# Brief: Intop Business — first-start PERMISSION steps (App Store 5.1.1 / Google Play review). Sign in, then READ-ONLY.

Read AGENT_BRIEF.md first: its tools, rules and report files apply. Budget: about 30 actions; write report.md and findings.json no later than action 28. Screenshot after EVERY action.
Never create, change, send, pay or delete anything. Never print credentials; write "the test password". The words "Hermes"/"Гермес" must never appear: report them if you see them.

## Sign in
Welcome → «У меня уже есть аккаунт» (scroll if needed). Tap the e-mail field, run `python3 scripts/<android|ios>/type_secret.py QA_FOOD_OWNER_EMAIL`, tap the password field, run it with `QA_FOOD_OWNER_PASSWORD`, then «Войти». If sign-in asks for anything else, stop and report a blocker.

## Permission steps (the point of this run) — write exactly what you see on each
1. After sign-in a first-start screen should explain notifications BEFORE any system dialog («Не пропустите заказ», examples of notifications, «Разрешить уведомления» and «Не сейчас»). Did a SYSTEM permission dialog appear before this explanation? (That would be a store-review failure.)
2. Tap «Разрешить уведомления». The system dialog appears: choose **Don't Allow / Не разрешать**. Screenshot. Does the app continue to the next step? Is there a line saying notifications are off and how to turn them on in Settings?
3. Sound step: tap «Оставить по умолчанию» (do NOT tap «Дальше» — it saves to the server).
4. «More permissions» step (camera, Live Activities, Face ID if shown): read every card. Is the purpose of each permission explained in plain words? If a camera button asks the system, choose **Don't Allow** and report what the app shows after it (a way to Settings? still usable?).
5. «Всё готово» → «Начать работу». Does the main screen open and work without notifications/camera? Open one screen that would use the camera (catalogue → add product photo / scanner) ONLY to look: after the refusal does it show a clear message and a way to Settings («Открыть настройки»)? Do not save anything.

## Report
AGENT_BRIEF.md format: one section per step with screenshot ids, the exact texts, the language, and PASS/FAIL against: explanation before the system prompt; refusal leaves the app usable; a path to Settings after refusal; no cut-off or untranslated text.
