"""Click at click-space coordinates. Usage: python scripts/desktop/click.py X Y [double|right] """
import sys, pyautogui
pyautogui.PAUSE = 0.2
x, y, mode = int(sys.argv[1]), int(sys.argv[2]), (sys.argv[3] if len(sys.argv) > 3 else "left")
w, h = pyautogui.size()
if not (0 <= x < w and 0 <= y < h):
    sys.exit(f"outside the screen ({w}x{h})")
pyautogui.moveTo(x, y, duration=0.15)
{"left": pyautogui.click, "double": pyautogui.doubleClick, "right": pyautogui.rightClick}[mode]()
print(f"{mode} click at ({x},{y}): check it on the next screenshot")
