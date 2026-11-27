# Brief: Intop Business iOS — login on small screens, «Начать работу», guest plurals, Studio «Готовые наборы» (Khan Chapan-test)

Read AGENT_BRIEF.md first: its tools, rules and final report files all apply. Budget: about 45 actions. Screenshot after every action.

## 1. Welcome and login layout
1. On the welcome screen write whether the logo, title, the 4 feature rows, «Продолжить» and «У меня уже есть аккаунт» are all fully visible without overlap or clipping. If the screen scrolls, scroll and report.
2. Tap «У меня уже есть аккаунт» / "I already have an account". On the login screen, BEFORE typing: are the e-mail field, password field, «Войти» and the footer links all reachable (scroll if needed)? Is anything clipped or overlapping?
3. Tap the e-mail field so the keyboard opens. Can you still scroll to «Войти» and the footer, or does the keyboard hide them with no way to reach them? Report exactly.
4. Run `python3 scripts/ios/type_secret.py QA_FOOD_OWNER_EMAIL`, tap the password field, run it with `QA_FOOD_OWNER_PASSWORD`, close the keyboard, tap «Войти». Never print or write these values; write "the test password". If a code, captcha or another account is asked, stop and report a blocker. Pick «Khan Chapan-test» if a business picker appears.

## 2. «Начать работу»
If a permissions/intro screen with «Начать работу» / "Start working" appears: tap it ONCE and screenshot immediately. Report whether the button at once shows a spinner (and no longer shows its label), and whether a second tap is ignored. Allow or skip system permission dialogs as they come ("Allow" for notifications is fine).

## 3. Guest counts and «Заказ ведёт»
1. Open «Заказы» / Orders and open any order (or a table, if the business has tables). Find a guest/seat count («1 гость», «2 гостя», «5 гостей» / "guests"). Write the exact texts you see; check the Russian word form matches the number (1 гость, 2–4 гостя, 5+ гостей; 11–14 гостей).
2. On the order screen, check the line «Заказ ведёт» / "Handled by": write how many times it appears on the screen (it must be at most once).

## 4. Studio «Готовые наборы» (read-only)
1. Find the mobile app builder: «Ещё» / More → «Studio» / «Приложение» (whatever opens the app canvas editor). If it is not there, report NOT REACHED with where you looked.
2. In the editor tap the add-block button («+» / «Добавить блок»). Scroll the sheet to the section «Готовые наборы» / "Ready-made sets".
3. Write every set title with its note and its block count label («3 блока», «5 блоков»…). Check the count words are correct Russian forms and that no text is cut off.
4. Do NOT tap a set and do NOT add any block. Close the sheet with «Закрыть» / the xmark.

## Never
Never publish, save, add or delete anything in Studio. Never send, accept or change orders, never pay, delete or change settings.

## Report
AGENT_BRIEF.md format. In report.md answer 1.1–1.4, 2, 3.1–3.2, 4.1–4.4 with PASS / FAIL / NOT REACHED and evidence (screenshot names, exact texts). `TEXT[ru]:` / `UI:` prefixes in findings.json.
