# Brief: Food pilot step 0 — owner reconnaissance in Intop Business iOS (Khan Chapan-test). READ-ONLY.

Read AGENT_BRIEF.md first. Budget: about 40 actions. Screenshot after every action. STRICTLY READ-ONLY: never create, send, pay, refund, delete, start or end anything, never change settings. Never generate codes.

## Login
Welcome → «У меня уже есть аккаунт». `python3 scripts/ios/type_secret.py QA_FOOD_OWNER_EMAIL` in e-mail, `QA_FOOD_OWNER_PASSWORD` in password (never print the values), «Войти». Pick «Khan Chapan-test». Skip intro steps and «Подключите Telegram» («Пропустить»).

## What to find and write down EXACTLY as shown (these feed the next steps of the pilot)
1. Hall / tables («Ещё» → «Зал и кухня» → «Столы» or «Зал»): list every table with its name/number, zone and status (free/occupied). Which tables look like TEST tables (name contains «тест»/«test»/«QA», or a note says so)? If none is marked, write that.
2. For ONE free test table (or, if none is marked, write «no test table»): open it and find its QR («QR-код стола», «Стол QR», share/link). Write the QR link URL text exactly if the app shows it (do not open it, do not regenerate it). If only an image is shown, describe and screenshot it.
3. Shift / cash («Касса и смены»): is a shift open now? Who opened it, when, cash in drawer. Read only.
4. Orders («Заказы»): how many orders are open now (new / in progress / ready), their numbers and tables.
5. Devices («Устройства» / «Касса»): which POS / kitchen devices are connected and their names. Do NOT create an enrollment code.
6. Team («Команда»): which staff exist with roles waiter / cook / cashier / manager (names only).
7. Stock («Склад»): is there a «Списание» (write-off) action and where; returns («Возвраты»): is there a refund action and where. Open the screens, do not confirm anything.

## Report
AGENT_BRIEF.md format. report.md: a section per item 1–7 with the exact names, numbers and screenshot ids. Mark anything you could not reach as NOT REACHED with the reason.
