"""Screenshot of the desktop + short status. Works on Linux (Xvfb), Windows and macOS.
Usage: python scripts/desktop/screen.py <dir> <NN>
Saves <dir>/<NN>.png scaled to at most 1280 px wide and prints how to convert
positions read on the image into click coordinates (what click.py expects)."""
import os, sys
from pathlib import Path
import mss, psutil, pyautogui
from PIL import Image

out, nn = Path(sys.argv[1]), sys.argv[2]
out.mkdir(parents=True, exist_ok=True)
with mss.mss() as s:
    shot = s.grab(s.monitors[1])
img = Image.frombytes("RGB", shot.size, shot.bgra, "raw", "BGRX")
cw, ch = pyautogui.size()           # click space (points on macOS, pixels elsewhere)
k = cw / min(img.width, 1280)
img.resize((round(cw / k), round(ch / k))).save(out / f"{nn}.png")
print(f"screenshot: {out}/{nn}.png (click space {cw}x{ch}; image {round(cw / k)}x{round(ch / k)}: multiply positions read on it by {k:.3f})")
print(f"mouse at {tuple(pyautogui.position())}")
pid = Path(os.environ.get("APP_PID_FILE", "results/app.pid"))
alive = pid.exists() and psutil.pid_exists(int(pid.read_text() or 0))
print("app process: " + ("running" if alive else "NOT RUNNING (crashed or closed): see results/*/app.log"))
log = Path(os.environ.get("APP_LOG", ""))
if not alive and log.is_file():
    print("last app log lines:\n" + "\n".join(log.read_text(errors="replace").splitlines()[-15:]))
