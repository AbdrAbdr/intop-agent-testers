# Brief: Intop Staff (waiter) — pilot fixes with one shift, FOOD test tenant Khan Chapan-test

Read AGENT_BRIEF.md first: its tools, rules and final report files all apply. Budget: about 35 actions, report-first: write report.md and findings.json NO LATER than action 35 (draft early, update at the end). Screenshot after every action.

## Hard safety rules (production backend, a live pilot runs in this tenant)
- You may write EXACTLY TWO things, both as the waiter account: (1) at the start «Начать смену» once (if asked for a zone, pick «Весь зал»); (2) at the very end «Завершить» / «Закончить смену» in the Profile and confirm «Закончить смену» in the sheet. Nothing else is written.
- NEVER send an order, never press «Проверить заказ», «На кухню», «Добавить к счёту», «Дозаказ», «Счёт», «Подать курс», «Забрал», «Убрал», «Иду», never take a guest call, never press «Отправить тестовое уведомление». Never pay, delete, invite, change settings, rotate PINs, print.
- Do NOT open order 261128-0001 or the table «Стол 12 QA Pilot 20261128» for any change; looking at the list is fine.
- Never print or write credentials; write "the test password".
- If ending the shift fails or you run out of actions before it, say so in the FIRST line of report.md: «SHIFT LEFT OPEN».
- Report text bugs as `TEXT[ru|uz|en]:` and layout/behaviour bugs as `UI:` in findings.json.

## Login
Welcome → «Войти» → «Почта» → e-mail: `python3 scripts/ios/type_secret.py QA_STAFF_WAITER_EMAIL`, password: same with `QA_STAFF_WAITER_PASSWORD` → «Войти». Onboarding: on «Не пропустите гостя» check the title and texts are whole (scroll if needed), tap «Позже»; on «Ещё разрешения» the «Разрешить» buttons are one line; go on to «Начать работу».

## Check (PASS / FAIL with a screenshot)
1. Start the shift (write 1). Then «Мои заказы»: a list, «Заказов пока нет», a spinner or an error — never blank. Table badges: short number in the dark square, a long name written in full next to it.
2. Segments «Заказы / Кухня / Бар» (only if orders exist): tall buttons, switch between them.
3. «Новый»: type 999 — status says there is no such table, the bottom button stays GREY. Clear with «C».
4. Step 1: the «Гостей» card with − / + under the keypad (local only). If no free tables, the line «Свободных столов нет — наберите номер стола» is above the keypad.
5. A FREE table chip (not table 12), if any: opens the menu with «Шаг 2 из 2 · Стол N · N гостя», «Блюда / Комбо», round «+». Add nothing. Back with the arrow.
6. Profile: «Начать» / «Завершить» look like 44 pt buttons. Notification settings: scroll to the very bottom — the black «Отправить тестовое уведомление» and its hint are fully visible above the bottom bar (do NOT press it). The «звук · сменить» links are tall enough to tap.
7. End the shift (write 2): Profile → «Завершить» → a sheet «Закончить смену?» must appear with a line about open orders (copy its text into the report) → «Закончить смену». Confirm the profile then says the shift is not started.
Languages follow the phone language; check every screen in it. In report.md list what you could not reach and why.
