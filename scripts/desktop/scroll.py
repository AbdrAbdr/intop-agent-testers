"""Scroll the mouse wheel at X Y. Usage: python scripts/desktop/scroll.py X Y down|up [clicks]"""
import sys, pyautogui
x, y, d = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
n = int(sys.argv[4]) if len(sys.argv) > 4 else 5
pyautogui.moveTo(x, y); pyautogui.scroll(-n if d == "down" else n)
print(f"scrolled {d} {n}")
