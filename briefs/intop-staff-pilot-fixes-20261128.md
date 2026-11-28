# Brief: Intop Staff (waiter) — check the 28.11 pilot fixes, READ ONLY, FOOD test tenant Khan Chapan-test

Read AGENT_BRIEF.md first: its tools, rules and final report files all apply. Budget: about 30 actions, report-first: write report.md and findings.json NO LATER than action 30 (draft early, update at the end). Screenshot after every action.

## Hard safety rules (production backend, a live pilot is running in this tenant)
- READ ONLY. NEVER start or end a shift (a waiter shift is already open — leave it), never send an order to the kitchen, never press «Проверить заказ», «На кухню», «Добавить к счёту», «Дозаказ», «Счёт», «Подать курс», «Забрал», «Убрал».
- NEVER press «Отправить тестовое уведомление». Never pay, delete, invite, change settings, rotate PINs, print.
- Do NOT open order 261128-0001 or the table «Стол 12 QA Pilot 20261128» for any change. Looking at the «Мои заказы» list is fine.
- Never print or write credentials; write "the test password".
- Report text bugs as `TEXT[ru|uz|en]:` and layout/behaviour bugs as `UI:` in findings.json; cut-off text, untranslated labels, raw keys, "UZS" instead of «сум», the words "Hermes"/"Гермес".

## Login
Welcome screen → «Войти» → switch «Телефон» to «Почта» → e-mail field: `python3 scripts/ios/type_secret.py QA_STAFF_WAITER_EMAIL`, password field: same with `QA_STAFF_WAITER_PASSWORD` → «Войти». Pick the workplace of Khan Chapan-test. If sign-in asks for anything else, stop and report a blocker. Allow notifications only if asked; on the permission screen «Позже» is fine.

## Check (each point: PASS / FAIL with a screenshot)
1. Login: the «Телефон / Почта» segment — each half is a full-height button (about 44 pt tall); «Позже» on the permission screen is a full-width button.
2. «Мои заказы»: the list is never blank — orders, «Заказов пока нет», a loading spinner or an error text. Table badges: a short number in the dark square; a long table name is written in full next to it, not cut to «12 QA…».
3. «Мои заказы» segments «Заказы / Кухня / Бар»: tall buttons (about 44 pt). Switch between them (reading only).
4. New order (tab «Новый» or «+»), step 1: type a number that does not exist (e.g. 999) — status says there is no such table and the black bottom button stays GREY («Выберите свободный стол»). Clear it with «C».
5. Step 1: the card «Гостей» with − and + under the keypad; tap + and − (local only, nothing is sent). If there are no free tables, the line «Свободных столов нет — наберите номер стола» sits above the keypad and is not covered by the bottom button.
6. If a FREE table chip is shown (not table 12): tap it to open the menu, check the subtitle «Шаг 2 из 2 · Стол N · N гостя», the «Блюда / Комбо» segment (tall buttons) and the round «+» buttons. Do NOT add dishes. Go back with the back arrow «Новый заказ».
7. Profile → notification settings: at the bottom either the black «Отправить тестовое уведомление» with a hint under it, or no such button (both are acceptable — do NOT press it). Report which.
Languages follow the phone language; check every screen in it. In report.md list what you could not reach and why.
