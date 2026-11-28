# Brief: Intop Business — touch areas after sign-in (Khan Chapan-test). READ-ONLY after sign-in.

Read AGENT_BRIEF.md first. Budget: about 30 actions. Screenshot after every action. Never create, change, send or pay anything.

1. Sign in: Welcome → «У меня уже есть аккаунт» (uz «Menda hisob bor»); `type_secret.py QA_FOOD_OWNER_EMAIL`, Return, `type_secret.py QA_FOOD_OWNER_PASSWORD`, sign in; pick «Khan Chapan-test».
2. The intro step «Подключите Telegram» (uz «Telegramni ulang»): report the size of «Пропустить» / «O‘tkazib yuborish» from the accessibility list (width × height, pt/dp). Then tap it once. Did it react on the first tap? Do NOT tap «Подключить».
3. Skip the other intro steps with their skip buttons.
4. Home: the hint card «Все разделы — под ручкой» (uz «Barcha bo‘limlar — tutqich ostida»): report the touch size of its close «×» / «Закрыть» from the accessibility list. Then tap the close once. Did the card close on the first tap? Does the card look the same as before otherwise (icon, title, text)?
5. Stop. Report sizes and first-tap results with screenshot ids.
