#!/usr/bin/env bash
# Downloads an encrypted test build from the builds release and decrypts it with BUILD_DECRYPT_KEY.
# Usage: bash scripts/fetch_build.sh <asset name without .enc> [release tag]
set -euo pipefail
NAME="$1"; TAG="${2:-builds-20261125}"
: "${BUILD_DECRYPT_KEY:?BUILD_DECRYPT_KEY secret is missing}"
gh release download "$TAG" -R "$GITHUB_REPOSITORY" -p "$NAME.enc" --clobber
printf '%s' "$BUILD_DECRYPT_KEY" | openssl enc -d -aes-256-cbc -pbkdf2 -in "$NAME.enc" -out "$NAME" -pass stdin
rm -f "$NAME.enc"
case "$NAME" in *.zip) ditto -x -k "$NAME" ios-app ;; esac
echo "build ready: $NAME"
