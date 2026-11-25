#!/usr/bin/env bash
# Prints the extra sentence of the agent prompt for reference / comparison runs (nothing for a normal run).
if [ -n "${IS_REF:-}" ]; then
  echo "THIS IS A REFERENCE RUN: you are the yardstick. Read briefs/reference-compare.md, section 'Reference run', and follow it."
elif [ -n "${REF_PERSONA:-}" ] && [ -d "reference/$REF_PERSONA" ]; then
  echo "REFERENCE COMPARISON: decrypted reference screenshots of the same app on the reference device are in reference/$REF_PERSONA/ (NN.png and report.md). Read briefs/reference-compare.md, section 'Comparison', and follow it."
fi
