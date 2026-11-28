# Brief: Food pilot step 5 — waiter ends own shift; read the order status (Intop Staff iOS, Khan Chapan-test)

Read AGENT_BRIEF.md first. Budget: about 25 actions. Screenshot after every action. Exactly ONE write: end the waiter's own shift. Nothing else (no payment, no order changes).

Login (waiter): «Войти», «Почта» / Email; `QA_STAFF_WAITER_EMAIL` / `QA_STAFF_WAITER_PASSWORD` via `python3 scripts/ios/type_secret.py` (never print). Pick «Khan Chapan-test».

1. «Заказы» / Orders: find order 261128-0001 (table «Стол 12 QA Pilot 20261128»). Write its exact status, total and items. Do NOT change it.
2. End the shift: «Закончить смену» / "End shift" (Orders tab or Profile). If the app refuses because of an open order or unpaid bill, screenshot the exact message and stop — do NOT pay or close the order.
3. Screenshot the result.

Report first lines: `ORDER 261128-0001: <status> <total>`, `WAITER SHIFT: CLOSED|REFUSED — <message>`.
