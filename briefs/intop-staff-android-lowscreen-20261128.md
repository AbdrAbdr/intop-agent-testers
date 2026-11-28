# Brief: Intop Staff Android (waiter) — step 1 of a new order on a low screen, demo mode

Read AGENT_BRIEF.md first. Budget about 25 actions, report-first by action 25. Screenshot after every action.
DEBUG build with a local demo: a pretend server inside the app answers every call; nothing leaves the phone; writes are refused locally.

Start: `adb shell am force-stop org.bytebit.intopstaff.dev; adb shell am start -n org.bytebit.intopstaff.dev/uz.intop.staff.MainActivity --es demo waiter`
Open the tab «Новый». Report PASS/FAIL with a screenshot for each:
1. On first view, WITHOUT scrolling: the number card («Номер стола», the big number, the status line) and the WHOLE keypad including the last row «АБВ/C · 0 · ⌫» are visible above the black bottom button. Nothing of the keypad is under the button.
2. Type 1, 0 (table 10): the number shows «10», the 0 key was reachable without scrolling, the number card did not move away.
3. Type 999 instead (clear with ⌫ / C first): status «Такого стола нет в вашей смене», button grey, keypad did not jump.
4. The area between the title «Новый заказ» and the number card scrolls on its own: the chips («Свободные» / «Недавние» or «Свободных столов нет…») and the «Гостей» card with − / + are there; scroll it; the number card and the keypad stay in place. Tap + and − on «Гостей».
5. Anything cut, overlapping or under 48 dp on this screen.
In report.md list what you could not reach and why.
