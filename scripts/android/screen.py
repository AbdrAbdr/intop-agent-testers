"""Screenshot of the emulator + list of visible elements.
Usage: python3 scripts/android/screen.py <dir> <NN>
Saves <dir>/<NN>.png at HALF size (cheaper to read) and prints each element
with its centre in REAL screen pixels, ready for `adb shell input tap X Y`.
Also prints crashes logged since the previous call, and an accessibility check
(controls with no name, touch targets under 48 dp) when the screen fails it."""
import io, os, re, subprocess, sys
import xml.etree.ElementTree as ET
from pathlib import Path
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import a11y  # noqa: E402

# Test credentials never reach the log, even when one lands in a visible field (stand 28.11: a password typed
# into the e-mail field was printed here). Every non-empty QA_* secret value is masked in all printed text.
_SECRETS = sorted({v for k, v in os.environ.items() if k.startswith("QA_") and v and len(v) >= 4}, key=len, reverse=True)


def _redact(text):
    # Mask every piece of a secret (5+ chars), not only the whole value: a password typed into the e-mail field
    # arrives glued to the address and cut at the print width, so a whole-value match misses it (stand 28.11, run 46129410596).
    for v in _SECRETS:
        for size in range(len(v), min(len(v), 5) - 1, -1):
            for i in range(len(v) - size + 1):
                if v[i:i + size] in text:
                    text = text.replace(v[i:i + size], "•••")
    return text



def adb(*a, raw=False):
    r = subprocess.run(["adb", *a], capture_output=True, timeout=60)
    return r.stdout if raw else r.stdout.decode("utf-8", "replace")


out, nn = Path(sys.argv[1]), sys.argv[2]
out.mkdir(parents=True, exist_ok=True)
png = adb("exec-out", "screencap", "-p", raw=True)
png = png[png.find(b"\x89PNG"):] if b"\x89PNG" in png else png  # foldables print a warning first
img = Image.open(io.BytesIO(png)).convert("RGB")
w, h = img.size
img.resize((w // 2, h // 2)).save(out / f"{nn}.png")
print(f"screenshot: {out}/{nn}.png (screen {w}x{h}; image is half size: multiply positions read on it by 2)")
adb("shell", "uiautomator", "dump", "/sdcard/ui.xml")
xml = adb("exec-out", "cat", "/sdcard/ui.xml")
try:
    root = ET.fromstring(xml[xml.find("<"):])
except ET.ParseError:
    root = ET.Element("hierarchy")
nodes = list(root.iter("node"))
for n in nodes:
    text, desc = (n.get("text") or "").strip(), (n.get("content-desc") or "").strip()
    edit = n.get("class", "").endswith("EditText")
    b = re.findall(r"\d+", n.get("bounds", ""))
    if not (text or desc or edit) or len(b) != 4:
        continue
    x1, y1, x2, y2 = map(int, b)
    kind = "field" if edit else ("button" if n.get("clickable") == "true" else "text")
    print(_redact(f"- {kind} \"{_redact(text or desc)[:70]}\" centre=({(x1 + x2) // 2},{(y1 + y2) // 2})"))
try:
    memo = Path(os.environ.get("RUNNER_TEMP", "/tmp")) / "density_dpi"
    if not memo.exists():
        dpi = re.findall(r"\d+", adb("shell", "wm", "density"))
        memo.write_text(dpi[-1] if dpi else "160")  # last one = override, if any
    check = a11y.android(root, int(memo.read_text()), w, h)
    if check:
        print(check)
except Exception:  # the check must never break seeing the screen
    pass
crash = adb("logcat", "-d", "-b", "crash") + adb("logcat", "-d", "AndroidRuntime:E", "ReactNativeJS:E", "*:S")
adb("logcat", "-c")
lines = [x for x in crash.splitlines() if x.strip() and not x.startswith("-----")]
if lines:
    print("ERRORS SINCE LAST SCREENSHOT:\n" + "\n".join(lines[-15:]))
