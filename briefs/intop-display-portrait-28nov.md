# Brief: Intop Display Android re-check on a STANDING tablet (28.11)

Read AGENT_BRIEF.md first: its tools, rules and final report files all apply. Budget: about 20 actions; write report.md and findings.json early and update them. Screenshot after every action.

## Hard safety rules (production backend, test tenants only)
- NEVER pay, enter card data, delete anything, change tenant or device settings, create enrollments, pair, or press print/test-print (the button «Test station printer» prints at once: never press it).
- Report text bugs as `TEXT[ru|uz|en]:` and layout bugs as `UI:` in findings.json. In report.md say for EACH check below: PASS or FAIL, with the screenshot number.

## Mode
First rotate the tablet to PORTRAIT: `adb shell settings put system accelerometer_rotation 0` then `adb shell settings put system user_rotation 1` (or 0, whichever gives a screen taller than wide; check with a screenshot). Package: `adb shell pm list packages | grep intop`.

## Checks
1. Connect screen: relaunch normally with `adb shell am start -S -n <package>/uz.intop.display.MainActivity`. In portrait the WHOLE pairing code must be visible on one line (for example «F72W-K9P3», not cut to «F72W-»), and the black button «Scan the code from Business» must show its whole text. Do not scan or pair.
2. Kitchen board: `adb shell am start -S -n <package>/uz.intop.display.MainActivity --es demo kitchen`. In portrait the board must show 2 ticket cards per row (not 4); ticket titles keep the table number («Table 7», «Table 3»); dish names are not broken in the middle of a word.
3. Gear → Settings: the row «Cards · N per row» must say 2 in portrait.
4. Rotate back to landscape and screenshot the board: up to 4 cards per row there.
