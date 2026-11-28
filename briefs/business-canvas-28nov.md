# Brief: Intop Business — order bill actions, Labels, tablet pages (Khan Chapan-test). READ-ONLY.

Read AGENT_BRIEF.md first. Budget: about 60 actions. Screenshot after every action.
STRICTLY READ-ONLY: a pilot is writing to this business right now. Never create, send, pay, refund, delete, close, split, print, accept, start or end anything, never change settings or toggles, never generate codes.
In particular NEVER tap «Печать счёта» / «Закрыть счёт» / «Разделить» / «Принять» / «Отменить» / «Вмешаться». Only look at them.

## Login
Welcome → «У меня уже есть аккаунт» (Uzbek: «Menda allaqachon akkaunt bor», English: «I already have an account»).
`type_secret.py QA_FOOD_OWNER_EMAIL` into e-mail, `QA_FOOD_OWNER_PASSWORD` into password (never print the values), sign in.
Pick «Khan Chapan-test». Skip intro steps and «Подключите Telegram» («Пропустить»). If the app was started in demo mode, use the demo business instead and say so.

## What to check (write exactly what you see)
1. Home. The title of the attention block. On a phone it should read «Требует внимания» (uz «E’tibor talab qiladi»); on a tablet (wide page with the left menu) «Ждут внимания» (uz «E’tibor kutmoqda», en «Waiting for you»). Any clipped, overlapping or untranslated text.
2. Orders. Open ONE order that is at a table (dine-in, a table number shown). Without tapping them, check:
   - a black pill «Печать счёта» (uz «Hisobni chop etish», en «Print the bill») next to the title, only while the bill is not paid;
   - under the dish lines a row: «Закрыть счёт» (black, about 2/3 width) and «Разделить» (light, about 1/3 width), height about the same as other big buttons;
   - nothing of that row on a delivery or pickup order (open one delivery/pickup order too if there is one).
   If no table order exists, write NOT REACHED and why.
3. More («Ещё») → group «Склад»: is «Этикетки» (uz «Yorliqlar») a row there, after «Рецепты»? Open it, screenshot, go back. On a tablet check the same row in the left menu.
4. Tablet only (iPad / Android tablet): open each of these and say for each whether the page uses the width (two columns, list | detail, grids) or looks like a phone layout stretched across the screen (one narrow column, or rows stretched edge to edge with empty space): Home, Orders (+ one order), Menu, Stock, Customers, Loyalty («Скидки и лояльность»), Team, Analytics, Settings, Notifications settings, Hall («Зал и брони»), Labels. On Orders / Customers / Team: roughly what share of the width the list takes (should be about 2/5).
5. Phone with large text: anything cut off on the order card (title, the pill, the button row).

## Report
AGENT_BRIEF.md format. report.md: a section per item 1–5 with screenshot ids. For item 4 a table: page | uses width? | what looks stretched. Mark anything you could not reach as NOT REACHED with the reason.
