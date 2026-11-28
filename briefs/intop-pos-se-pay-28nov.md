# Brief: Intop POS iPhone SE — cash pay summary above the keypad (28.11)

Read AGENT_BRIEF.md first: its tools, rules and final report files all apply. Budget: about 15 actions; write report.md and findings.json early and update them. Screenshot after every action.

## Hard safety rules (production backend, test tenants only)
- NEVER pay with real data, enter card data, delete anything, change tenant or device settings, create enrollments, invite staff, or press print/test-print. Demo payments are fake and fine.
- Report layout bugs as `UI:` and text bugs as `TEXT[ru|uz|en]:` in findings.json. In report.md say for EACH check: PASS or FAIL, with the screenshot number.

## Mode
On the Connect screen tap the small bottom link «Посмотреть демо» (scroll down if needed). Demo data is fake.

## Checks
1. Sale: add 2–3 dishes, open the cart, «Оплатить», «Наличные». Screenshot before typing.
2. Type 200000 on the keypad. The summary card must scroll by itself so that its rows «Получено 200 000 сум» and «Сдача …» are fully visible right above the keypad area, and the pinned line «Получено … · Сдача …» is shown over the keys. Nothing of the card may be half-cut at the edge of the keypad area. Screenshot.
3. Erase a few digits so the sum is short: the line must say «Не хватает …» in red. Screenshot. Do not press «Принять наличные».
