"""Types text into the focused field, replacing what is there (select-all first).
Usage: python scripts/desktop/type.py "text"   (click the field first)"""
import shutil, subprocess, sys, pyautogui

def type_text(t):
    pyautogui.PAUSE = 0.05
    pyautogui.hotkey("command" if sys.platform == "darwin" else "ctrl", "a")
    pyautogui.press("backspace")
    if shutil.which("xdotool"):                     # Linux: handles Cyrillic and accents
        subprocess.run(["xdotool", "type", "--delay", "40", "--", t], check=False)
    else:
        pyautogui.write(t.encode("ascii", "ignore").decode(), interval=0.03)   # ponytail: ASCII only on Windows/macOS

if __name__ == "__main__":
    type_text(sys.argv[1]); print("typed: check it on the next screenshot")
