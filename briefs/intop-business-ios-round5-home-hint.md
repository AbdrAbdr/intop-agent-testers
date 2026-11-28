# Brief: Intop Business iOS — round 5: the Home hint (Khan Chapan-test)

Read AGENT_BRIEF.md first: its tools, rules and final report files all apply. Budget: about 30 actions. Screenshot after every action. Read-only.

## 1. Login
Welcome → «У меня уже есть аккаунт». `python3 scripts/ios/type_secret.py QA_FOOD_OWNER_EMAIL` in e-mail, `QA_FOOD_OWNER_PASSWORD` in password (never print the values), «Войти». Pick «Khan Chapan-test» if asked. Go through the intro steps; on «Подключите Telegram» tap «Пропустить» (never «Подключить»).

## 2. Home right after the setup
Is any POPOVER bubble (floating, with an arrow) on Home? (It must not be.) Is there an inline hint CARD in the page flow near the top (about the handle / «ручка»)? Quote its text. Does anything on Home sit under it or get covered?
Tap «Неделя» once with the hint on screen: did the period switch on the FIRST tap?

## 3. Close the hint
Tap the hint's ✕. Does the «Потяните вниз, чтобы обновить» card take its place? Then open the handle above the tab bar once, go back to Home and pull to refresh: are both hints gone?

## Report
AGENT_BRIEF.md format. Answer 2 and 3 with PASS / FAIL and screenshots. `UI:` / `TEXT[ru|uz|en]:` prefixes in findings.json.
