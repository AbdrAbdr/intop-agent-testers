# Brief: Food pilot step 1b — owner adds ONE test table (Intop Business iOS, Khan Chapan-test)

Read AGENT_BRIEF.md first. Budget: about 25 actions. Screenshot after every action. Exactly ONE write: one new table. Nothing else.

Login: «У меня уже есть аккаунт» / "I already have an account", `QA_FOOD_OWNER_EMAIL` / `QA_FOOD_OWNER_PASSWORD` via `python3 scripts/ios/type_secret.py` (never print), «Войти». Pick «Khan Chapan-test». Skip intro and Telegram («Пропустить» / Skip).

Steps:
1. Open the Tables screen: search field on Home «Найти или спросить Intop» / "Find or ask Intop" → type «Столы» / "Tables", or More → «Зал» / "Hall" / «Столы».
2. Tap «Добавить стол» / "Add table". Name: `Стол 12 QA Pilot 20261128`, capacity 4, zone: the main hall («Основной зал») if asked. Save.
3. Screenshot the list with the new table; write its exact name and status (must be free).

Never: edit or delete any other table, regenerate QR codes, touch orders.
Report first line: `TABLE: CREATED <name>` or `TABLE: FAIL — <reason>`.
