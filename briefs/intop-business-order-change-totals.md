# Brief: Intop Business, «Изменить заказ» totals preview (Khan Chapan-test)

Read AGENT_BRIEF.md first: its tools, rules and final report files all apply. Budget: about 35 actions. Screenshot after every action.

## Login
Welcome screen: tap «У меня уже есть аккаунт» / "I already have an account". Tap the e-mail field, run `python3 scripts/<android|ios>/type_secret.py QA_FOOD_OWNER_EMAIL`, tap the password field, run the same with `QA_FOOD_OWNER_PASSWORD`, close the keyboard, tap «Войти». Never print or write these values; write "the test password". If a code, captcha or other account is asked, stop and report a blocker. Pick «Khan Chapan-test» if a business picker appears.

## The check (read-only: you must NOT send anything)
Order **261125-0001** has two dishes: «Ассорти булочек» 34 000 сум and «Фанта 0,25л» 23 000 сум, total 57 000 сум, not paid.
1. Open «Заказы», find order 261125-0001 (search by number if there is a search) and open it. Write down the total shown.
2. Open «Изменить заказ». Choose the action «Убрать позицию» (Remove item) and select ONLY «Фанта 0,25л». Reason: «Закончилось».
3. Wait 2 seconds. Find the block «Итог» with «Было» and «Станет» (scroll inside the sheet if needed). Write down every row and amount exactly. Expected: «Было» 57 000 сум, «Станет» 34 000 сум; no «Вернём гостю» row because the order is not paid (or 0). Say PASS/FAIL for each number. The currency must be a word/symbol («сум»), not "UZS".
4. A «PIN менеджера» field may appear (the dish is already in the kitchen). Do NOT type any PIN. Just note whether it appeared.
5. Now also select «Ассорти булочек» (both dishes chosen). Wait 2 seconds. Expected: the totals disappear and a red text says «Это последняя позиция. Чтобы убрать её, отмените весь заказ.» and «Отправить гостю» is disabled — OR the totals simply disappear (older build). Write down exactly what you see.
6. Close the sheet WITHOUT sending («Закрыть» / back / swipe down). Reopen the order: no new proposal / «Ожидает ответа гостя» must appear.

## Never
NEVER tap «Отправить гостю» / "Send to guest" or any confirm. Never type a PIN, never change order status, never pay, delete or change settings.

## Report
AGENT_BRIEF.md format. In report.md answer each of the 6 steps with PASS / FAIL / NOT REACHED and the evidence (screenshot names, exact texts and amounts). `TEXT[ru]:` / `UI:` prefixes in findings.json.
