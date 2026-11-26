# Brief: Intop Kiosk, targeted check (Android, landscape 1080p)

Read AGENT_BRIEF.md first: its tools, rules and final report files all apply. Budget: at most 12 actions, screenshot after every action. Write report.md and findings.json by action 10.

Safety: debug fake data only. Never pay, enter a real PIN, change settings or print. Never print credentials.

The run launched the debug demo (menu with sample items). Package: `adb shell pm list packages | grep intopkiosk` (usually org.bytebit.intopkiosk.dev). Screen is landscape 1280x720 dp.

Steps:
1. On the menu, open the category «Роллы» (it has ONE dish). Check the dish card is normal size (one tile-width card, not a half-screen square), and its name and price are fully visible ABOVE the «Мой заказ» bar.
2. Open the staff PIN dialog: `adb shell am start -S -n <package>/uz.intop.kiosk.MainActivity --es kioskDemo staff`. Check the WHOLE dialog is visible without scrolling, including the bottom «Отмена» button under «Войти» (title, text, PIN dots, keypad, both buttons). Do not type a PIN.
3. Report each check as PASS or FAIL with the screenshot number; write report.md and findings.json (UI: for layout bugs).
