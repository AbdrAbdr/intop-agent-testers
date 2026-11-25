#!/usr/bin/env bash
# macOS: switch the hosted display to the largest mode that fits inside WxH (modes are fixed by the runner:
# 640x480 ... 1920x1080; 1366x768, 1280x800 and 2560x1440 do not exist, so 1344x756, 1280x720 and 1920x1080 are used).
# Usage: bash scripts/desktop/set_resolution_macos.sh 1366x768     Prints the mode in force afterwards.
set -uo pipefail
WANT=${1:?WxH}; brew list displayplacer >/dev/null 2>&1 || brew install displayplacer >/dev/null 2>&1
LIST=$(displayplacer list 2>/dev/null)
ID=$(printf '%s\n' "$LIST" | awk '/Persistent screen id/{print $4; exit}')
MODE=$(printf '%s\n' "$LIST" | python3 -c "
import re,sys
W,H=map(int,'$WANT'.split('x'))
m=[tuple(map(int,x)) for x in re.findall(r'res:(\d+)x(\d+) hz:60',sys.stdin.read())]
fit=[r for r in m if r[0]<=W and r[1]<=H] or [min(m)]
w,h=max(fit,key=lambda r:r[0]*r[1]); print(f'{w}x{h}')")
echo "wanted $WANT, closest available $MODE"
displayplacer "id:$ID res:$MODE hz:60 color_depth:7 scaling:off origin:(0,0) degree:0" 2>&1 | tail -2
sleep 2; displayplacer list | grep -E "Resolution:" | head -1
