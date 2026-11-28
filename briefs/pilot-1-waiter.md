# Brief: Food pilot step 1 — waiter takes ONE order at a QA table (Intop Staff iOS, Khan Chapan-test)

Read AGENT_BRIEF.md first. Budget: about 40 actions. Screenshot after every action. This brief allows exactly ONE write: one new hall order sent to the kitchen. Nothing else.

## Login (waiter)
Fresh install: «Войти», switch «Телефон» → «Почта». E-mail field: `python3 scripts/ios/type_secret.py QA_STAFF_WAITER_EMAIL`; password field: same with `QA_STAFF_WAITER_PASSWORD`; «Войти». Never print the values. Pick «Khan Chapan-test» if asked. Allow/skip system dialogs.

## The one order
1. Open the tables / hall view. Pick table **«Стол 10 QA Launch»** (if absent, «Стол 9 QA 20261110»; if neither, stop and report). Do NOT touch any existing order on that table.
2. Start a NEW order for that table, guests: 2.
3. Add exactly TWO cheap dishes from two different categories, quantity 1 each (the two cheapest you can see quickly; avoid weighted items). Write their names and prices.
4. Send the order to the kitchen («Отправить на кухню» / «В работу» / the main send button). Screenshot the result.
5. Write down EXACTLY: the new order number (e.g. 261128-000X), table, items, total, time. This number is the input for the next pilot steps.

## Never
No payment, no bill request, no cancel, no second order, no change to other orders, no shift actions. If sending fails, screenshot the error and stop (no retry more than once).

## Report
AGENT_BRIEF.md format. report.md first line: `ORDER: <number> | TABLE: <name> | ITEMS: <a>, <b> | TOTAL: <sum>` or `ORDER: NOT CREATED — <reason>`. Then UI/TEXT findings.
