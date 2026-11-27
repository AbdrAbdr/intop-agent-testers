# Brief: Intop Business, «Изменить заказ» after a cook's report (Khan Chapan-test)

Read AGENT_BRIEF.md first: its tools, rules and final report files all apply. Budget: about 40 actions. Screenshot after every action.

## Login
Welcome screen: tap «У меня уже есть аккаунт» / "I already have an account". Tap the e-mail field, run `python3 scripts/<android|ios>/type_secret.py QA_FOOD_OWNER_EMAIL`, tap the password field, run the same with `QA_FOOD_OWNER_PASSWORD`, close the keyboard, tap «Войти». Never print or write these values; write "the test password". If a code, captcha or other account is asked, stop and report a blocker. Pick «Khan Chapan-test» if a business picker appears.

## The check (read-only: you must NOT send anything)
A cook has reported that the dish «Барбекю» (15 000 сум) of order **261125-0005** is out of stock and suggested a replacement.
1. Open «Заказы» and find order 261125-0005 (search by number if there is a search). Open it.
2. Look for a kitchen note on the order or on the line «Барбекю»: «Кухня сообщила» / "Kitchen reported" with the reason and the suggested replacement. Write down its exact text and any button on it.
3. Open «Изменить заказ» (Change order), from the kitchen card if it has a button, otherwise from the order screen.
4. Check the PREFILL: is «Барбекю» already chosen, is the action «Заменить», is the replacement dish the one the cook suggested, is the reason «Закончилось»? Write down what is preselected and what is empty.
5. Check the PREVIEW block «Было / Станет / Вернём гостю» (or «Доплата»): write down all amounts exactly as shown. "Было" must be 15 000 сум (the order total). "Станет" = the order with the replacement. The difference must equal "Вернём гостю" (if cheaper) or "Доплата" (if more expensive). Say whether the numbers add up. Check the currency is a word/symbol, not "UZS".
6. If the comment field is empty, type `QA` (2 letters) and see whether the send button becomes disabled or shows a hint; then type `QA проверка` and see it enabled. Do NOT tap the send button.
7. Close the sheet WITHOUT sending: use «Отмена» / back / swipe down. Confirm discarding if asked. Reopen the order and check that no new proposal / «Ожидает ответа гостя» appeared.

## Never
NEVER tap «Отправить гостю» / "Send to guest" or any confirm of the change. Never accept/withdraw proposals, never change the order status, never pay, delete or change settings.

## Report
AGENT_BRIEF.md format. In report.md answer each of the 7 steps with PASS / FAIL / NOT REACHED and the evidence (screenshot names, exact texts and amounts). `TEXT[ru]:` / `UI:` prefixes in findings.json.
