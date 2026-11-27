# Brief: Intop Business iOS — round 3 recheck (Khan Chapan-test)

Read AGENT_BRIEF.md first: its tools, rules and final report files all apply. Budget: about 40 actions. Screenshot after every action. Read-only: never send, accept, pay, delete or change settings.

## 1. Login with the keyboard
Welcome → «У меня уже есть аккаунт» / "I already have an account". Tap the e-mail field. Are the password field and «Войти» visible right above the keyboard without scrolling? Write yes/no with the screenshot.
Then run `python3 scripts/ios/type_secret.py QA_FOOD_OWNER_EMAIL`, tap the password field, run it with `QA_FOOD_OWNER_PASSWORD`, close the keyboard, tap «Войти». Never print or write these values. Pick «Khan Chapan-test» if a business picker appears.

## 2. Intro steps after login (notifications, sound, more permissions, ready)
On EACH step: is any card or text hidden under the pinned bottom buttons? If the page continues below, is there a visible hint (a fade above the buttons, a scroll bar flash)? Scroll to the end and write whether everything is reachable. On the camera/other permissions step: is «Разрешить» / "Allow" written on one line (not broken as «Разре-шить»)? On «Начать работу» tap once and screenshot at once.
Allow or skip system dialogs as they come.

## 3. «Ещё» / More
Open «Ещё» → the full list of sections. Are row captions readable (up to two lines, no «…» cutting the meaning)? Write 3 examples.

## Never
Never tap send/confirm/pay/delete, never change settings or data.

## Report
AGENT_BRIEF.md format. In report.md answer 1, 2 (per step), 3 with PASS / FAIL / NOT REACHED and evidence. `UI:` / `TEXT[ru]:` prefixes in findings.json.
