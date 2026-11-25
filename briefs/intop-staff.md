# Brief: Intop Staff (waiter / kitchen app), FOOD test tenant Khan Chapan-test

Read AGENT_BRIEF.md first: its tools, rules and final report files all apply. Budget: about 30 actions, and report-first: write report.md and findings.json NO LATER than action 30 (draft them early, update at the end). Screenshot after every action.

## Hard safety rules (production backend, test tenants only)
- NEVER pay, enter card data, delete anything, change tenant or device settings, rotate PINs, create enrollments, invite staff, or press print/test-print. Reading a screen is fine.
- Never print or write credentials; write "the test password".
- Report text bugs as `TEXT[ru|uz|en]:` and layout/behaviour bugs as `UI:` in findings.json; also: untranslated or mixed labels, raw keys, cut-off text, wrong currency format (a word like "сум", never "UZS"), the words "Hermes"/"Гермес" (must never appear). Note the device type (phone or tablet) and whether the layout uses the space.
- In report.md list what you could NOT reach and why.

## Login (real account, no code needed)
Fresh install shows the welcome screen «Добро пожаловать в Intop Staff» with «Войти» and «У меня есть приглашение». Do NOT use the invitation path (needs a live invite).
Tap «Войти», switch the toggle from «Телефон» to «Почта». Tap the e-mail field, then run `python3 scripts/<android|ios>/type_secret.py QA_STAFF_WAITER_EMAIL`, tap the password field, run the same with `QA_STAFF_WAITER_PASSWORD`, then «Войти». TABLET personas (lucia, jonas, mateo, minjun) use `QA_STAFF_COOK_EMAIL` / `QA_STAFF_COOK_PASSWORD` instead (kitchen role). Phone code/SMS sign-in is not testable: do not use it.
If sign-in wants anything else (code, captcha), stop, report as blocker and test the welcome/sign-in screens only (wrong password `wrong-password-1` for the error text). After sign-in pick the workplace «Место работы» of Khan Chapan-test.
Do NOT start or end a shift, send or fire orders, change a table or order status, or snooze/clear real notifications: only open and read.

## Cover (waiter): tab bar, «Заказы», tables, «Входящие» (calls), a check/bill screen (do not request the bill), «Профиль», language/notification settings. Cook: «Кухня» board, station/tickets, problem report sheet (open, do not send). Tablet: judge the tablet layout (panes, rail, wasted space), rotate if possible.
Languages follow the phone language (ru/uz/en): check every screen you see in that language.
