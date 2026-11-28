# Brief: Food pilot step 2 — kitchen cooks ONE order (Intop Staff iOS, cook, Khan Chapan-test)

Read AGENT_BRIEF.md first. Budget: about 30 actions. Screenshot after every action. Allowed writes: only moving the tickets of order **261128-0001** (table «Стол 12 QA Pilot 20261128») through the kitchen stages to «Готово». Plus starting the cook's own shift if the app requires it (do NOT end it). Nothing else. The UI may be in English: «Кухня»=Kitchen, «Начать»=Start, «Готово»=Ready, «Начать смену»=Start shift.

## Login (cook)
«Войти», «Телефон» → «Почта». `python3 scripts/ios/type_secret.py QA_STAFF_COOK_EMAIL` / `QA_STAFF_COOK_PASSWORD`, «Войти». Never print the values. Pick «Khan Chapan-test».

## Steps
1. Open «Кухня» (kitchen board). Find the ticket(s) of order 261128-0001 with «Garlic Croutons» and «Suzma with Vegetables» (RU names may differ). If not there within 2 minutes (pull to refresh), stop and report which tickets you see.
2. For each of its dishes: start («Начать» / «Готовить»), then mark ready («Готово»). Screenshot each change.
3. Screenshot the final state of the ticket and write the time.

## Never
Do not touch any other ticket, the stop-list, problems or shifts.

## Report
First line: `KITCHEN: <order> READY at <time>` or `KITCHEN: FAILED — <reason>`. Then UI/TEXT findings.
