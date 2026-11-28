# Brief: Intop Staff — first-start PERMISSION steps (App Store 5.1.1 / Google Play review), FOOD test tenant Khan Chapan-test. Sign in, then READ-ONLY.

Read AGENT_BRIEF.md first: its tools, rules and report files apply. Budget: about 30 actions; write report.md and findings.json no later than action 28. Screenshot after EVERY action.
Never pay, start/end a shift, send orders, change statuses, delete anything or press print. Never print credentials; write "the test password". The words "Hermes"/"Гермес" must never appear.

## Sign in
Welcome «Добро пожаловать в Intop Staff» → «Войти» (NOT the invitation path). Switch «Телефон» → «Почта». Tap the e-mail field, run `python3 scripts/<android|ios>/type_secret.py QA_STAFF_WAITER_EMAIL`, tap the password field, run it with `QA_STAFF_WAITER_PASSWORD`, «Войти». Pick the workplace of Khan Chapan-test if asked. If sign-in wants a code/captcha, stop and report a blocker.

## Permission steps (the point of this run) — write exactly what you see on each
1. Where in the flow does Staff first explain notifications/camera? Did any SYSTEM permission dialog appear before an in-app explanation? (That would be a store-review failure.)
2. On the notifications explanation tap the allow button; in the system dialog choose **Don't Allow / Не разрешать**. Screenshot. Does the app continue? Is there a line about Settings and a working «Открыть настройки»? (Tapping it may open system Settings: then come back to the app.)
3. Camera explanation (scanner): allow → in the system dialog choose **Don't Allow**. What does the app show? Still usable?
4. Reach the main screen (orders/tables tab bar). Open the scanner or any camera entry ONLY to look: after the refusal is there a clear message and a path to Settings? Do not scan or send anything.

## Report
AGENT_BRIEF.md format: one section per step with screenshot ids, exact texts, language, and PASS/FAIL against: explanation before the system prompt; refusal leaves the app usable; a path to Settings after refusal; no cut-off or untranslated text.
