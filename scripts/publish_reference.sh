#!/usr/bin/env bash
# Run on YOUR machine after `bash scripts/collect.sh <run id>` of a run with the ref-* personas:
# packs their screenshots + report.md, encrypts with the BUILD_DECRYPT_KEY key file and uploads the result as the
# release asset reference-<app>-<run id>.tgz.enc (public repo, but only the encrypted file is public).
# Usage: BUILD_KEY_FILE=/path/to/key bash scripts/publish_reference.sh <run id> <app> [release tag]
# <app> is a short slug of the app under test, e.g. business-food, business-market, staff, pos, kiosk, display.
# The key is read from the file and never printed.
set -euo pipefail
RUN="${1:?run id}"; APP="${2:?app slug}"; TAG="${3:-builds-20261125}"
[[ "$RUN" =~ ^[0-9]+$ && "$APP" =~ ^[a-z0-9-]+$ ]] || { echo "bad run id or app slug"; exit 1; }
KEY="${BUILD_KEY_FILE:?set BUILD_KEY_FILE to the file that holds the BUILD_DECRYPT_KEY value}"
[ -s "$KEY" ] || { echo "key file is missing or empty"; exit 1; }
ROOT=$(cd "$(dirname "$0")/.." && pwd); SRC="$ROOT/runs/$RUN"
[ -d "$SRC" ] || { echo "$SRC not found: run scripts/collect.sh $RUN first"; exit 1; }
STAGE=$(mktemp -d); trap 'rm -rf "$STAGE"' EXIT
N=0
for ref in $(python3 -c "import json;print(' '.join(p['id'] for p in json.load(open('$ROOT/personas.json')) if p.get('reference')))"); do
  dir="$SRC/$ref/results/$ref"; [ -d "$dir" ] || continue
  mkdir -p "$STAGE/$ref"; cp "$dir"/*.png "$STAGE/$ref/" 2>/dev/null || true
  [ -f "$dir/report.md" ] && cp "$dir/report.md" "$STAGE/$ref/"
  c=$(ls "$STAGE/$ref"/*.png 2>/dev/null | wc -l | tr -d ' '); echo "$ref: $c screenshots"; N=$((N + c))
done
[ "$N" -gt 0 ] || { echo "no reference screenshots in $SRC (expected runs/$RUN/<ref persona>/results/<ref persona>/NN.png)"; exit 1; }
OUT="$STAGE/reference-$APP-$RUN.tgz.enc"
tar czf - -C "$STAGE" $(cd "$STAGE" && ls -d */) | openssl enc -aes-256-cbc -pbkdf2 -salt -out "$OUT" -pass "file:$KEY"
gh release upload "$TAG" "$OUT" --clobber -R "$(gh repo view --json nameWithOwner -q .nameWithOwner)"
echo "published reference-$APP-$RUN.tgz.enc ($N screenshots). Use: -f reference_run=$RUN"
