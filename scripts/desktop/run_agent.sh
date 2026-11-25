#!/usr/bin/env bash
# Runs on the desktop runner (Linux under xvfb-run, Windows in Git Bash, macOS):
# launches the POS jar windowed, then hands the screen to Claude Code.
# Output goes to results/ (encrypted later), never to the public log.
# Env: OS_NAME PERSONA_ID LANG_CODE THEME DEMO BRIEF MODEL JAR (+ LLM_*, QA_*)
set -uo pipefail
PERSONA="${OS_NAME}-${LABEL:-$PERSONA_ID}"; export PERSONA
mkdir -p "results/$PERSONA"
export APP_PID_FILE="$PWD/results/app.pid" APP_LOG="$PWD/results/$PERSONA/app.log"
ARGS=(--window "${RES:-1920x1080}" --lang "$LANG_CODE" --theme "$THEME"); [ "${DEMO:-true}" = true ] && ARGS+=(--demo)
[ -n "${ROLE:-}" ] && ARGS+=(--role "$ROLE")
[ -n "${APP_ARGS:-}" ] && ARGS+=($APP_ARGS)
[ -n "${EXTRA_ARGS:-}" ] && ARGS+=($EXTRA_ARGS)   # word-split on purpose: --window 1080x1920
java -jar "$JAR" "${ARGS[@]}" > "$APP_LOG" 2>&1 &
echo $! > "$APP_PID_FILE"
sleep 20
python scripts/desktop/screen.py "results/$PERSONA" 00 > "results/$PERSONA/launch-check.txt" 2>&1 || true
python -c "import pyautogui;print('requested ${RES:-?}, actual %dx%d' % tuple(pyautogui.size()))" > "results/$PERSONA/resolution.txt" 2>&1; cat "results/$PERSONA/resolution.txt" | sed 's/^/screen: /'
head -4 "results/$PERSONA/launch-check.txt" | grep -v '^mouse' | sed 's/^/launch: /'
source scripts/llm_env.sh || exit 1
claude -p "Read $BRIEF and personas.json, then do the mission until the final report. PERSONA=$PERSONA (results folder; persona id $PERSONA_ID) PLATFORM=desktop OS=$OS_NAME. $(cat "results/$PERSONA/resolution.txt"; [ -n "${ROLE:-}" ] && echo "; app role $ROLE"; [ -n "${SECOND_SCREEN:-}" ] && echo "; a second screen $SECOND_SCREEN sits to the right of the first: the screenshot shows both, click positions on it are in the same combined space, see briefs/intop-pos-desktop-dual.md"). App language $LANG_CODE, theme $THEME, demo mode ${DEMO:-true}. A first screenshot is already saved as results/$PERSONA/00.png: start your numbering at 01. Budget: about 30 actions; after each screen append one line to results/$PERSONA/notes.md; write report.md and findings.json no later than action 30 (the run is cut off at a hard turn limit)." \
  --model "${MODEL:-sonnet}" --max-turns ${MAX_TURNS:-60} --output-format json \
  --allowedTools "Bash(python scripts/desktop/screen.py:*),Bash(python scripts/desktop/click.py:*),Bash(python scripts/desktop/key.py:*),Bash(python scripts/desktop/scroll.py:*),Bash(python scripts/desktop/type.py:*),Bash(python scripts/desktop/type_secret.py:*),Bash(sleep:*),Bash(ls:*),Bash(cat:*),Bash(mkdir:*),Read,Write,Edit" \
  > results/agent-output.json 2> results/agent-errors.txt
CODE=$?

# report_fallback: if the turn limit cut the agent off before report.md, write it from the evidence
if [ ! -s "results/$PERSONA/report.md" ]; then
  claude -p "The test agent for PERSONA=$PERSONA ran out of turns before writing its report. Read notes.md (if any) and look at every screenshot in results/$PERSONA, then write results/$PERSONA/report.md and results/$PERSONA/findings.json in the format the brief $BRIEF asks for. Report only what the screenshots show; mark anything uncertain." \
    --model "${MODEL:-sonnet}" --max-turns 25 --output-format json \
    --allowedTools "Read,Write,Bash(ls:*)" > results/agent-output-fallback.json 2>> results/agent-errors.txt || true
fi
python scripts/agent_status.py results/agent-output.json results/agent-errors.txt "$PERSONA" || true
kill "$(cat "$APP_PID_FILE")" 2>/dev/null
echo "Agent finished (exit $CODE), $(ls "results/$PERSONA" | wc -l) files"
