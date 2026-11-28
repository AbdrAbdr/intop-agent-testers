# Brief: Food pilot step 3 — cashier: split bill, cash, refund, close shift (Intop Staff iOS, Khan Chapan-test)

Read AGENT_BRIEF.md first. Budget: about 50 actions. Screenshot after every action. Allowed writes ONLY on order **261128-0001** (table «Стол 12 QA Pilot 20261128», total 88 000 сум) and the cashier's own shift. Nothing else. The UI may be in English: «Касса»=Register/Cashier, «Разделить поровну»=Split equally, «Наличные»=Cash, «Возврат»=Refund, «Открыть/Закрыть смену»=Open/Close shift.

## Login
«Войти», «Телефон» → «Почта». Use `QA_FOOD_OWNER_EMAIL` / `QA_FOOD_OWNER_PASSWORD` with `python3 scripts/ios/type_secret.py` (never print them). Pick «Khan Chapan-test». If the app does not offer a cashier / «Касса» workplace for this account, write `CASHIER: NO ROLE` with screenshots and stop.

## Steps
1. Shift: if no shift is open, open one («Открыть смену»), opening cash 0. Write the time.
2. Open order 261128-0001 in the cashier list.
3. Split the bill «Разделить поровну» into 2 guests. Screenshot both parts and amounts.
4. Take payment for part 1 in CASH («Наличные»), entering exactly its amount. Then the same for part 2. Screenshot the paid state.
5. Refund: in the same order open «Возврат», refund ONE dish (the cheaper one) in cash, reason «Тест пилота». Screenshot the result and the amounts.
6. At the end, also check the waiter/cook shifts are not touched. Close ONLY the cashier shift («Закрыть смену»), counting the cash the app expects. Screenshot the Z/summary and any discrepancy.

## Never
No card payments, no other orders, no discounts, no deleting. If a step fails, screenshot the error text, do NOT retry more than once, and continue with the next step if it does not depend on it.

## Report
First lines: `SPLIT: PASS|FAIL`, `CASH: PASS|FAIL`, `REFUND: PASS|FAIL`, `SHIFT CLOSE: PASS|FAIL`, each with screenshot ids and error text. Then UI/TEXT findings.
