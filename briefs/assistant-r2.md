# Brief: Intop Business — Assistant, round 2 (layout fixes) — iOS owner (Khan Chapan-test) / Android demo

Read AGENT_BRIEF.md first. Budget: about 40 actions. Screenshot after every action. Never confirm an action card («Подтвердить» / Confirm): tap «Отмена» / Cancel.

iOS login: «У меня уже есть аккаунт», `QA_FOOD_OWNER_EMAIL` / `QA_FOOD_OWNER_PASSWORD` via `python3 scripts/ios/type_secret.py` (never print), «Войти», «Khan Chapan-test», skip intro and Telegram. Android: demo mode, no login.

1. Home → pills: measure the tap target of each pill with the accessibility tree / `scripts/a11y.py` — must be ≥44 pt high.
2. «Ассистент»: is the input bar at the bottom edge (no big empty gap under it, only the home-indicator margin)? Are all 4 suggestions and the footer note fully visible above the input? Is the placeholder readable (not cut)?
3. Android only: tap the input — the keyboard opens. Do the pills stay visible at the top? Does only the input move up?
4. Ask «Сводка за сегодня» (Android demo: the answer comes from a demo stream). Does the text appear progressively? Then ask «Покажи таблицу продаж» (Android: should render a real table with columns), then «Собери отчёт файлом» (Android: a file card XLSX/PDF with «Хранится до …»), then «Поставь плов на стоп» (Android: an action card — tap «Отмена»).
5. History: «Новый чат» — does it work on the FIRST tap?
6. Does any word break with a hyphen in the middle in answers (iOS)?

Report: per step PASS/FAIL with screenshot ids and measured sizes; `UI:`/`TEXT[ru|uz|en]:` findings.
