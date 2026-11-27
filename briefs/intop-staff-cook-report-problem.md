# Brief: Intop Staff, cook reports one kitchen problem (Khan Chapan-test)

Read AGENT_BRIEF.md first: its tools, rules and final report files all apply. Budget: about 30 actions. Screenshot after every action.
This brief overrides one rule of `briefs/intop-staff.md`: you DO send exactly ONE problem report, on exactly ONE named dish. Nothing else is sent.

## Login (kitchen role)
Fresh install shows «Добро пожаловать в Intop Staff». Tap «Войти», switch «Телефон» to «Почта». Tap the e-mail field, run `python3 scripts/android/type_secret.py QA_STAFF_COOK_EMAIL`, tap the password field, run the same with `QA_STAFF_COOK_PASSWORD`, then «Войти». Never print or write these values; write "the test password". If sign-in wants a code or captcha, stop and report a blocker. Pick the workplace of «Khan Chapan-test» if asked.

## The one action you may send
1. Open «Кухня» (kitchen board). Find the ticket of order **261125-0005** (the number may show as «0005» or «#261125-0005») with the dish **«Барбекю»**. Scroll or use filters if needed. If it is not there, stop: report which orders you see and send nothing.
2. Open the dish and tap «Проблема» (Problem).
3. Reason: «Закончилось» (out of stock). Action: «Убрать блюдо» (Remove the dish). This is only a suggestion: the order is NOT changed, a manager decides later. The sheet opens at half height: swipe up inside it until «Сообщить гостю» is visible.
4. Then tap «Сообщить гостю» once. Screenshot the result.
5. Look at how the ticket looks afterwards (held / waiting for decision). Do not touch any other ticket.

## Never
Do not start, bump, finish, recall or cancel any ticket. Do not change the stop-list. Do not start or end a shift. Do not send a second report; if the first one fails, screenshot the error and stop.

## Report
AGENT_BRIEF.md format. In report.md state clearly: was the report sent (yes/no), the exact reason and action, the time, and any error text. Also list `TEXT[ru]:` / `UI:` issues you saw on these screens.
