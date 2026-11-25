"""Types a test credential from the environment without exposing it.
Usage: python scripts/desktop/type_secret.py QA_FOOD_OWNER_EMAIL
Only QA_* variable names are accepted; the value is never printed."""
import os, re, sys
from type import type_text

name = sys.argv[1] if len(sys.argv) == 2 else ""
if not re.fullmatch(r"QA_[A-Z0-9_]{1,60}", name) or not os.environ.get(name):
    sys.exit("unknown or empty test credential name")
type_text(os.environ[name]); print("typed " + name + ": check it on the next screenshot")
