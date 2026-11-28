# Brief: Food pilot step 4 — owner writes off ONE stock item (Intop Business iOS, Khan Chapan-test)

Read AGENT_BRIEF.md first. Budget: about 25 actions. Screenshot after every action. Exactly ONE write: one write-off of 1 unit (or the smallest allowed amount) of ONE stock item.

Login: «У меня уже есть аккаунт», `QA_FOOD_OWNER_EMAIL` / `QA_FOOD_OWNER_PASSWORD` via `python3 scripts/ios/type_secret.py` (never print them), «Войти», «Khan Chapan-test». Skip intro and Telegram («Пропустить»).

Steps: More → «Склад и стоп-лист» → «Склад» → «Списание». Pick an item that HAS stock (not «закончился»), prefer a cheap ingredient (salt, napkins, water). Quantity 1 (smallest unit). Reason «Тест пилота» / «Порча» if a reason list exists. Confirm. Then open «История» and screenshot the write-off line. Write item, quantity, unit, stock before/after.

Never: anything else. Report first line `WRITE-OFF: PASS <item> <qty> before→after` or `WRITE-OFF: FAIL — <reason>`.
