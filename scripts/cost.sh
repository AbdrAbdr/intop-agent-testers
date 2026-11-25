#!/usr/bin/env bash
# Sums total_cost_usd of every agent of a collected run (after scripts/collect.sh).
# Usage: bash scripts/cost.sh <run id>
set -euo pipefail
python3 - "$(cd "$(dirname "$0")/.." && pwd)/runs/${1:?run id}" <<'PY'
import glob, json, os, sys
root, total = sys.argv[1], 0.0
for f in sorted(glob.glob(f"{root}/*/results/agent-output.json")):
    try: c = float(json.load(open(f)).get("total_cost_usd") or 0)
    except Exception: c = 0.0
    total += c; print(f"{os.path.basename(os.path.dirname(os.path.dirname(f))):40s} ${c:.3f}")
print(f"{'TOTAL':40s} ${total:.3f}")
PY
