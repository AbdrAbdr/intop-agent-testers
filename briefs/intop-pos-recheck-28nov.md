# Brief: Intop POS re-check after fixes (28.11)

Read AGENT_BRIEF.md first: its tools, rules and final report files all apply. Budget: about 25 actions; write report.md and findings.json early and update them. Screenshot after every action.

## Hard safety rules (production backend, test tenants only)
- NEVER pay with real data, enter card data, delete anything, change tenant or device settings, create enrollments, invite staff, or press print/test-print. Demo payments are fake and fine.
- Report text bugs as `TEXT[ru|uz|en]:` and layout bugs as `UI:` in findings.json. In report.md say for EACH check below: PASS or FAIL, with the screenshot number.

## Mode
On the Connect screen tap the small bottom link «Посмотреть демо» (scroll down if needed). Demo data is fake.

## Checks
1. «Заказы» → order №98. Below the dish there is a red card «Гость не ответил · решите сами» and a button «Оставить как было». Tap the button once: the card must change to «Гость не ответил — заказ без изменений» and the button must disappear.
2. Sale: add 2–3 dishes. On a tablet the cart on the right must show each dish NAME and price (not only a grey square and a stepper).
3. Pay (cash): the summary («Итого» / «Получено» / «Сдача») must be visible above the number keypad without scrolling; type 200000 and check «Сдача» is visible. On a tablet the left order column must show «Итого» and the sum on one line (not broken letter by letter).
4. On a tablet: «Смена» screen — the left column labels and amounts readable (not «Открыт…», «Вн…»); «Заказы» → №98 in the right pane — the dish name readable.
