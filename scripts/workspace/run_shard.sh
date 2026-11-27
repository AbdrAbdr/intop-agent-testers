#!/usr/bin/env bash
# Runs on the macOS runner. Public logs: prints ONLY counts. Everything readable goes to results/ (encrypted afterwards).
# Usage: bash run_shard.sh <asset name without .enc> <release tag> <shard i> <shard n>
set -uo pipefail
ASSET=$1; TAG=$2; I=$3; N=$4
: "${BUILD_DECRYPT_KEY:?BUILD_DECRYPT_KEY secret is missing}"
ROOT=$PWD; mkdir -p results ws
gh release download "$TAG" -R "$GITHUB_REPOSITORY" -p "$ASSET.enc" --clobber >/dev/null 2>&1 || { echo "download failed"; exit 1; }
printf '%s' "$BUILD_DECRYPT_KEY" | openssl enc -d -aes-256-cbc -pbkdf2 -in "$ASSET.enc" -pass stdin | tar xz -C ws || { echo "decrypt failed"; exit 1; }
rm -f "$ASSET.enc"
# Official Node.js for the agent sandbox (same pin and sha256 as the app: docs RELEASE.md, e2e section).
D=$HOME/.cache/intop-e2e/node-v22.23.4; mkdir -p "$D/dl" "$D/x"
curl -sSfLo "$D/dl/node.tar.gz" https://nodejs.org/dist/v22.23.4/node-v22.23.4-darwin-arm64.tar.gz || { echo "node download failed"; exit 1; }
echo "c9e1dbc748b33ed2d14f42445191ecaf14c56259c7a9a26d0042c49ec2b66428  $D/dl/node.tar.gz" | shasum -a 256 -c - >/dev/null || { echo "node sha mismatch"; exit 1; }
tar -xzf "$D/dl/node.tar.gz" -C "$D/x"
cd ws
npm ci --no-audit --no-fund >"$ROOT/results/npm-ci.log" 2>&1 || { echo "npm ci failed"; tail -n 40 "$ROOT/results/npm-ci.log" >/dev/null; }
cd app
git config --global user.email e2e@example.com; git config --global user.name e2e
PURPLEFLOW_HIDDEN=1 CI=1 npx playwright test --workers=1 --shard="$I/$N" >"$ROOT/results/list.log" 2>&1
echo "playwright exit=$?"
cp e2e-report.json "$ROOT/results/" 2>/dev/null; cp -R e2e-results "$ROOT/results/" 2>/dev/null
node -e '
const r=require(process.argv[1]);let p=0,f=0,k=0,fl=0;
(function w(s){(s.specs||[]).forEach(x=>x.tests.forEach(t=>{const o=t.status;if(o==="expected")p++;else if(o==="flaky")fl++;else if(o==="skipped")k++;else f++;}));(s.suites||[]).forEach(w)})({suites:r.suites});
console.log(`RESULT shard ${process.argv[2]}: passed=${p} flaky=${fl} failed=${f} skipped=${k}`)' "$PWD/e2e-report.json" "$I/$N" 2>/dev/null || echo "RESULT: no report"
