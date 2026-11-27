#!/usr/bin/env bash
# Run LOCALLY: downloads and decrypts the Workspace e2e artifacts of a run. Usage: collect.sh <run_id> [out_dir]
set -euo pipefail
RUN=$1; OUT=${2:-$HOME/intop-artifacts/workspace-gh-e2e-$1}; PRIV=${PRIV:-$HOME/.mobile-agent-testers/AbdrAbdr_intop-agent-testers.pem}
mkdir -p "$OUT/enc"
gh run download "$RUN" -R AbdrAbdr/intop-agent-testers -D "$OUT/enc" --pattern "results-workspace-e2e-*"
for key in "$OUT"/enc/*/*.key.bin; do
  name=$(basename "$key" .key.bin); dir=$(dirname "$key")
  pass=$(openssl pkeyutl -decrypt -inkey "$PRIV" -pkeyopt rsa_padding_mode:oaep -in "$key")
  mkdir -p "$OUT/$name"; openssl enc -d -aes-256-cbc -pbkdf2 -in "$dir/$name.tgz.enc" -pass "pass:$pass" | tar xz -C "$OUT/$name"
done
echo "decrypted into $OUT"
