# Brief: Food pilot step 4b — receive ONE unit, then write off THE SAME batch (Intop Business iOS, Khan Chapan-test)

Read AGENT_BRIEF.md first. Budget: about 40 actions. Screenshot after every action. Exactly TWO writes: (1) one stock receipt of 1 unit of one cheap item on branch «Main» / «Основной»; (2) one write-off of that same unit from that same batch. Nothing else. Never touch any old batch.

Login: «У меня уже есть аккаунт» / "I already have an account", `QA_FOOD_OWNER_EMAIL` / `QA_FOOD_OWNER_PASSWORD` via `python3 scripts/ios/type_secret.py` (never print), «Войти». Pick «Khan Chapan-test». Skip intro and Telegram.

Before any write: screenshot the business name and the selected branch, and write them down (must be Khan Chapan-test / Main). If the branch is not Main, switch to Main first.

1. More → «Склад и стоп-лист» / "Stock & stop list" → «Склад» → «Приход» / "Receive". Receive manually (not by photo): ONE cheap item (e.g. salt, water, napkins), quantity 1 (smallest unit), price as small as allowed, supplier if required: any test supplier already in the list. Branch / warehouse: Main. Save. Write: item, quantity, unit, warehouse, any document or batch number shown.
2. Open the item: stock must now be 1. Write down the batch identifier or date if shown.
3. «Списание» / "Write-off": the SAME item, quantity 1, reason «Тест пилота» / «Порча» if a reason list exists. Confirm.
4. «История» / History: screenshot both lines (receipt and write-off). Stock must be back to the previous value.

Never: change or write off any other batch, especially old ones without a branch. If a step fails, screenshot the error text and stop.
Report first lines: `RECEIPT: PASS|FAIL <item> <qty> <doc/batch id>`, `WRITE-OFF: PASS|FAIL <qty> <doc id>`, `STOCK: <before> → <after receipt> → <after write-off>`, `TENANT/BRANCH: <seen>`.
