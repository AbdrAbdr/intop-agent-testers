"""Screenshot of the iOS simulator + visible elements (AXe accessibility tree).
Usage: python3 scripts/ios/screen.py <dir> <NN>
The PNG is resized to the screen size in POINTS, so a position read on the
image goes straight to `bash scripts/ios/gesture.sh tap X Y`. Also warns
when the app is no longer running or a crash report just appeared, and prints an
accessibility check (controls with no name, touch targets under 44 pt)."""
import io, json, os, shutil, subprocess, sys, tempfile, time
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


def capture_png(shoot):
    """The raw screen never lands in the artifacts folder: it is written to a private 0700 temp dir outside it, read into memory
    and removed in `finally`, also when the capture or the read fails (Bold 28.11)."""
    d = tempfile.mkdtemp(prefix="intop-shot-")
    try:
        os.chmod(d, 0o700)
        path = os.path.join(d, "raw.png")
        shoot(path)
        with open(path, "rb") as f:
            return f.read()
    finally:
        shutil.rmtree(d, ignore_errors=True)


def mask(img, els, scale, secrets=None):
    """Pixels too (Bold 28.11): every input field is painted over BEFORE the PNG is written, and so is any element whose text
    holds a piece of a secret (a password typed into the e-mail field, cut or not). No tree → nothing proves the screen is clean →
    the whole screen is withheld. A frame partly off the screen is clipped to it."""
    global _SECRETS
    if secrets is not None:
        _SECRETS = secrets
    from PIL import ImageDraw
    draw = ImageDraw.Draw(img)
    W, H = img.size
    if not els:
        draw.rectangle([0, 0, W, H], fill=(0, 0, 0))
        return
    for kind, label, value, f in els:
        if not f or f.get("width", 0) <= 0 or f.get("height", 0) <= 0:
            continue
        text = label + " " + value
        # Editable inputs only: read-only text (SwiftUI Text, a UITextView used for unhyphenated labels) stays visible;
        # a secret piece in ANY element is still painted by the text match.
        if "Field" in kind or kind == "TextArea" or _redact(text) != text:
            x, y, w, h = (f.get(k, 0) * scale for k in ("x", "y", "width", "height"))
            box = [max(0, x), max(0, y), min(W, x + w), min(H, y + h)]
            if box[0] < box[2] and box[1] < box[3]:
                draw.rectangle(box, fill=(0, 0, 0))


UDID, APP = os.environ["UDID"], os.environ.get("APP_ID", "")


def run(*a):
    return subprocess.run(list(a), capture_output=True, text=True, timeout=60).stdout


def walk(n, acc):
    if isinstance(n, list):
        for c in n:
            walk(c, acc)
        return
    if not isinstance(n, dict):
        return
    f, label = n.get("frame") or {}, (n.get("AXLabel") or n.get("title") or "").strip()
    value, kind = str(n.get("AXValue") or "").strip(), (n.get("type") or n.get("role_description") or "").strip()
    if f and (label or value or "Field" in kind or kind in ("Button", "TextArea")):
        acc.append((kind, label, value, f))
    walk(n.get("children") or [], acc)


out, nn = Path(sys.argv[1]), sys.argv[2]
out.mkdir(parents=True, exist_ok=True)
try:
    tree = json.loads(run("axe", "describe-ui", "--udid", UDID))
except json.JSONDecodeError:
    tree = []
els = []
walk(tree, els)
img = Image.open(io.BytesIO(capture_png(lambda path: run("xcrun", "simctl", "io", UDID, "screenshot", "--type=png", path)))).convert("RGB")
memo = Path(os.environ.get("RUNNER_TEMP", "/tmp")) / "width_points"
root = tree[0] if isinstance(tree, list) and tree else tree
wpt = int((root.get("frame") or {}).get("width", 0)) if isinstance(root, dict) else 0
if wpt >= 300 and img.size[0] % wpt == 0:
    memo.write_text(str(wpt))           # app in front: trust its frame
elif memo.exists():
    wpt = int(memo.read_text())         # system alert / home screen: reuse
else:
    wpt = img.size[0] // 3
scale = img.size[0] / wpt
hpt = img.size[1] / scale
if _SECRETS:
    mask(img, els, scale)
img.resize((round(img.size[0] / scale), round(hpt))).save(out / f"{nn}.png")
print(f"screenshot: {out}/{nn}.png ({wpt}x{round(hpt)} points; positions on the image = positions to tap)")
seen = set()
for kind, label, value, f in els:
    if kind in ("Application", "Window", "ScrollBar") or f.get("width", 0) <= 0:
        continue
    cx, cy = round(f["x"] + f["width"] / 2), round(f["y"] + f["height"] / 2)
    if not (0 <= cx <= wpt and 0 <= cy <= hpt) or (label, value, cx, cy) in seen:
        continue
    seen.add((label, value, cx, cy))
    name = "field" if "Field" in kind or kind == "TextArea" else ("button" if kind in ("Button", "Link", "Switch", "Cell", "Tab") else "text")
    extra = f" value \"{_redact(value)[:40]}\"" if value and value != label else ""
    print(_redact(f"- {name} \"{_redact(label or value)[:70]}\"{extra} centre=({cx},{cy})"))
try:
    a11y.REDACT = _redact
    check = a11y.ios(tree, wpt, hpt)
    if check:
        print(_redact(check))
except Exception:  # the check must never break seeing the screen
    pass
if APP and APP not in run("xcrun", "simctl", "spawn", UDID, "launchctl", "list"):
    print("WARNING: the app is no longer running (crash or closed).")
reports = Path.home() / "Library/Logs/DiagnosticReports"
for p in (reports.glob("*.ips") if reports.exists() else []):
    if time.time() - p.stat().st_mtime < 120:
        print(f"CRASH REPORT: {p.name} (less than 2 min ago)")
