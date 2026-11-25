#!/usr/bin/env bash
# CI: downloads the encrypted reference screenshots of a finished reference run and decrypts them into reference/<persona>/.
# The asset is reference-<app>-<run id>.tgz.enc on the builds release (AES-256, key = BUILD_DECRYPT_KEY secret);
# the decrypted files stay on the runner: results are encrypted separately and reference/ is never uploaded.
# Usage: bash scripts/fetch_reference.sh <reference run id> <reference persona id> [release tag]
set -euo pipefail
RUN="$1"; REF="$2"; TAG="${3:-${REFERENCE_TAG:-builds-20261125}}"
[[ "$RUN" =~ ^[0-9]+$ ]] || { echo "reference_run must be a run id (digits)"; exit 1; }
: "${BUILD_DECRYPT_KEY:?BUILD_DECRYPT_KEY secret is missing}"
NAME=$(gh release view "$TAG" -R "$GITHUB_REPOSITORY" --json assets -q '.assets[].name' | grep -E "^reference-.*-$RUN\.tgz\.enc$" | head -1 || true)
[ -n "$NAME" ] || { echo "::error::no asset reference-<app>-$RUN.tgz.enc in release $TAG: run scripts/publish_reference.sh $RUN <app> first"; exit 1; }
mkdir -p reference; TMP="${RUNNER_TEMP:-/tmp}/ref"; mkdir -p "$TMP"
gh release download "$TAG" -R "$GITHUB_REPOSITORY" -p "$NAME" --dir "$TMP" --clobber
printf '%s' "$BUILD_DECRYPT_KEY" | openssl enc -d -aes-256-cbc -pbkdf2 -in "$TMP/$NAME" -pass stdin | tar xz -C reference "$REF"
rm -f "$TMP/$NAME"
[ -d "reference/$REF" ] || { echo "::error::$NAME has no screenshots of $REF"; exit 1; }
echo "reference ready: reference/$REF ($(ls reference/$REF/*.png 2>/dev/null | wc -l | tr -d ' ') screenshots)"
