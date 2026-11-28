# Brief: Intop Business iOS — round 4: tips, the Telegram step, Day/Week/Month (Khan Chapan-test)

Read AGENT_BRIEF.md first: its tools, rules and final report files all apply. Budget: about 40 actions. Screenshot after every action. Read-only: never send, accept, pay, delete or change settings.

## 1. Login
Welcome → «У меня уже есть аккаунт» / "I already have an account". Run `python3 scripts/ios/type_secret.py QA_FOOD_OWNER_EMAIL` in the e-mail field and `QA_FOOD_OWNER_PASSWORD` in the password field (never print or write the values), tap «Войти». Pick «Khan Chapan-test» if a picker appears. Go through the intro steps (allow or skip system dialogs).

## 2. Setup steps right after login (phone and/or «Подключите Telegram»)
While a setup sheet is on screen: is ANY tip bubble (popover with a title and an arrow, e.g. «Заказы в работе», «Все разделы») visible anywhere? Write yes/no with the screenshot.
On «Подключите Telegram» / "Connect Telegram": before scrolling, is any text visible THROUGH or UNDER the bottom buttons («Подключить», «Пропустить»)? Scroll to the end: is all text reachable above the buttons? Then tap «Пропустить» / "Skip" (never «Подключить»).

## 3. Home
On Home right after the sheet closes: is a tip bubble shown? If yes, what does it say and does it cover Home content (the revenue card, order rows)? Then open «Меню» and «Склад» tabs: is a «Заказы в работе» bubble shown there? (It must not be.)

## 4. Day / Week / Month on Home
Use the accessibility tree / `scripts/a11y.py` to read the frame height of each of «День», «Неделя», «Месяц» (or the UZ/EN words). Write the three heights in pt. Tap «Неделя», screenshot: did the number change period and is the selected pill clearly visible?

## Never
Never tap send/confirm/pay/delete/«Подключить», never change settings or data.

## Report
AGENT_BRIEF.md format. In report.md answer 2, 3, 4 with PASS / FAIL / NOT REACHED and evidence (screenshot names). `UI:` / `TEXT[ru|uz|en]:` prefixes in findings.json.
