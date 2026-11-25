"""Press keys or combos in order. Usage: python scripts/desktop/key.py enter tab ctrl+a F11 esc
(cmd works on macOS; ctrl+a is mapped to cmd+a there.) Scroll: key.py pagedown, or scroll.py."""
import sys, pyautogui
pyautogui.PAUSE = 0.2
for combo in sys.argv[1:]:
    keys = combo.lower().split("+")
    if sys.platform == "darwin":
        keys = ["command" if k == "ctrl" else k for k in keys]
    pyautogui.hotkey(*keys)
print("pressed " + " ".join(sys.argv[1:]))
