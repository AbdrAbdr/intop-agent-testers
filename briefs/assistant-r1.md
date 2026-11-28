# Brief: Intop Business — Assistant, round 1 (Khan Chapan-test owner, iOS) / demo (Android)

Read AGENT_BRIEF.md first. Budget: about 45 actions. Screenshot after every action. Do NOT confirm any action card («Подтвердить» / Confirm): tap «Отмена» / Cancel if one appears. Ask only questions that read data.

iOS login: «У меня уже есть аккаунт», `QA_FOOD_OWNER_EMAIL` / `QA_FOOD_OWNER_PASSWORD` via `python3 scripts/ios/type_secret.py` (never print), «Войти», «Khan Chapan-test», skip intro and Telegram. Android: the app starts in demo mode (no login).

1. Home: are there two pills on top «Главная | Ассистент» (UZ «Asosiy | Yordamchi» or similar, EN «Home | Assistant»)? Do they fit on one line, ≥44 pt high?
2. Tap «Ассистент». Is the bottom tab bar gone and replaced by an input with «+», microphone and send? Are there 4 ready suggestions? Is the word «Hermes»/«Гермес» anywhere? (Must not be.)
3. Tap the suggestion «Сводка за сегодня» (or type it). Does the answer appear progressively (word by word) or all at once? Is there a status line while waiting, and a «Стоп» button instead of send? Screenshot during and after. Is the answer about this business (numbers, orders)?
4. Type «Покажи таблицу продаж по блюдам за неделю». Is a table rendered (columns, not raw `|` pipes)?
5. Tap the microphone: does it ask for microphone permission / show a recording panel with timer and «Отмена / Готово»? Tap «Отмена».
6. Open the history (top-left icon): search, «Новый чат», the 90-day note. Tap «Новый чат».
7. Turn off Wi-Fi is not possible; skip network errors.
8. Back to «Главная»: is the tab bar back?

Report: per step PASS/FAIL with screenshot ids; `UI:` / `TEXT[ru|uz|en]:` findings; quote the exact answer text of step 3 (first 3 lines).
