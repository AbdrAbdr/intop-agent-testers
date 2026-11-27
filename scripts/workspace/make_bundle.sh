#!/usr/bin/env bash
# Run LOCALLY from a built worktree of the private repo. Produces an encrypted e2e bundle (no sources, no secrets).
# Usage: bash make_bundle.sh <worktree> <out_dir> [short_sha]
# Needs: npm ci done in the worktree, ~/.mobile-agent-testers/build.key
set -euo pipefail
WT=$(cd "$1" && pwd); OUT=$2; SHA=${3:-$(git -C "$WT" rev-parse --short=8 HEAD)}
KEY=${BUILD_KEY_FILE:-$HOME/.mobile-agent-testers/build.key}
export PATH="$HOME/.intop/node/bin:$PATH"
mkdir -p "$OUT"; S=$(mktemp -d "$OUT/stage.XXXXXX"); trap 'rm -rf "$S"' EXIT
if [ -z "${SKIP_BUILD:-}" ]; then
  (cd "$WT" && npm run build -w @purpleflow/core >/dev/null && cd app && npx electron-vite build >/dev/null)
fi
mkdir -p "$S/app/e2e" "$S/core" "$S/scripts"
cp -R "$WT/app/out" "$S/app/out"
cp "$WT/package.json" "$WT/package-lock.json" "$S/"; cp "$WT/scripts/fix-node-pty.mjs" "$S/scripts/"
cp "$WT/app/package.json" "$S/app/"; cp "$WT/core/package.json" "$S/core/"; cp -R "$WT/core/prompts" "$S/core/prompts"
cp -R "$WT/app/.srt-stage" "$WT/app/.tool-resources" "$S/app/"   # staged runtimes: node scripts/stage-{sandbox,openspec}-runtime.mjs (--dev) in the worktree
cp "$WT/app/e2e/fake-claude.mjs" "$S/app/e2e/"
# Specs import app/src and core/src (ipc ids, i18n): inline only what they use, third-party packages stay external.
cd "$WT"
for f in app/e2e/*.spec.ts; do
  npx esbuild "$f" --bundle --platform=node --format=cjs --target=node22 --packages=external \
    --outfile="$S/app/e2e/$(basename "${f%.ts}").js" --log-level=error
done
cat > "$S/app/playwright.config.js" <<'CFG'
const { defineConfig } = require('@playwright/test');
module.exports = defineConfig({
  testDir: './e2e', testMatch: '**/*.spec.js', workers: 1, timeout: 120000, expect: { timeout: 20000 },
  retries: 1, outputDir: 'e2e-results',
  testIgnore: ['**/update-signed-mac-stage.spec.js', '**/dictation-native.spec.js'],
  reporter: [['json', { outputFile: 'e2e-report.json' }], ['list']],
  use: { trace: 'retain-on-failure', screenshot: 'only-on-failure' },
});
CFG
# Hard guards: nothing private may slip in.
if find "$S" -path '*/src/*' -o -name '*.p12' -o -name '*.pem' -o -name '*.key' -o -name '*.p8' -o -name .git | grep -q .; then
  echo "FORBIDDEN file in bundle" >&2; find "$S" -path '*/src/*' -o -name '*.p12' -o -name '*.pem' -o -name '*.key' -o -name '*.p8' | head; exit 1; fi
tar czf "$OUT/bundle.tar.gz" -C "$S" .
openssl enc -aes-256-cbc -pbkdf2 -salt -in "$OUT/bundle.tar.gz" -out "$OUT/workspace-e2e-$SHA.tar.gz.enc" -pass "file:$KEY"
rm -f "$OUT/bundle.tar.gz"; ls -lh "$OUT/workspace-e2e-$SHA.tar.gz.enc"; (cd "$S" && ls)
