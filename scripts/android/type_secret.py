"""Types a test credential from the environment without exposing it.
Usage: python3 scripts/android/type_secret.py QA_FOOD_OWNER_EMAIL
Only QA_* variable names are accepted; the value is never printed."""
import os, re, subprocess, sys

name = sys.argv[1] if len(sys.argv) == 2 else ""
if not re.fullmatch(r"QA_[A-Z0-9_]{1,60}", name) or not os.environ.get(name):
    sys.exit("unknown or empty test credential name")
r = subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), "type.py"), os.environ[name]],
                   capture_output=True, text=True)
print("typed " + name + ": check it on the next screenshot" if r.returncode == 0 else "failed to type " + name)
