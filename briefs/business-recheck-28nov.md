# Brief: Intop Business — recheck of the 28.11 fixes (Khan Chapan-test). READ-ONLY.

Read AGENT_BRIEF.md first. Budget: about 50 actions. Screenshot after every action.
STRICTLY READ-ONLY: a pilot writes to this business. Never create, send, pay, refund, delete, close, split, print, post, accept, start or end anything, never change settings or toggles, never generate codes.
NEVER tap «Печать счёта» / «Закрыть счёт» / «Разделить» / «Провести» / «Списать» / «Принять» / «Отменить» / «Вмешаться». Only look at them.

## Login
Welcome → «У меня уже есть аккаунт» (uz «Menda hisob bor», en «I already have an account»). `type_secret.py QA_FOOD_OWNER_EMAIL` into e-mail, `QA_FOOD_OWNER_PASSWORD` into password (never print values), sign in, pick «Khan Chapan-test», skip the intro.
1. Login with the keyboard open: after you type the e-mail, tap the password field. Is the WHOLE password field visible above the «Войти»/«Kirish» button, or partly under it? Screenshot with the keyboard open.

## Checks (write exactly what you see)
2. Home: scroll down slowly. Does any content show through under the clock / status bar at the top, or does the top strip stay plain page colour?
3. Orders: open ONE table order (dine-in). Is the order number visible in the top bar? Where is the black «Печать счёта» pill (top bar, or first row of the card at the right)? Its height (≥ 44 pt?). Do NOT tap it.
4. Same order: under the dish lines «Закрыть счёт» (≈2/3) and «Разделить» (≈1/3) — present, one line each?
5. More → «Этикетки»: is the page title «Этикетки» visible? Does the product list show names WITHOUT a « · Default» ending? Go back, then open «Модификаторы» (Modifiers) the same way and compare: does Modifiers show its title? Screenshot both.
6. More → «QR-коды столов» / «QR столов»: tap one table tile (NOT a print button) to open its sheet. Is there a link written as text on one line (cut in the middle with «…»)? Are there two buttons «Скопировать ссылку» and «Поделиться», each ≥ 44 pt? Do NOT tap Share, Print or the signed-link button. Long table names in the grid: do they wrap to two lines instead of «…»?
7. «Лояльность» / «Скидки и лояльность»: does it open without an error? What blocks are on it (discount groups, happy hours, points programme)?
8. Android only: open any order with a change history («Изменения»): are dates in the app language (Russian «нояб.», not «nov»)? Notification settings: does the card say «На этом устройстве»?

## Report
AGENT_BRIEF.md format. report.md: a section per item 1–8 with screenshot ids; NOT REACHED with the reason where needed.
