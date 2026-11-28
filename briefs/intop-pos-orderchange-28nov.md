# Brief: Intop POS (cash register), demo mode

Read AGENT_BRIEF.md first: its tools, rules and final report files all apply. Budget: about 30 actions, and report-first: write report.md and findings.json NO LATER than action 30 (draft them early, update at the end). Screenshot after every action.

## Hard safety rules (production backend, test tenants only)
- NEVER pay, enter card data, delete anything, change tenant or device settings, rotate PINs, create enrollments, invite staff, or press print/test-print. Reading a screen is fine.
- Never print or write credentials; write "the test password".
- Report text bugs as `TEXT[ru|uz|en]:` and layout/behaviour bugs as `UI:` in findings.json; also: untranslated or mixed labels, raw keys, cut-off text, wrong currency format (a word like "сум", never "UZS"), the words "Hermes"/"Гермес" (must never appear). Note the device type (phone or tablet) and whether the layout uses the space.
- In report.md list what you could NOT reach and why.

## Mode
A fresh install shows «Подключение кассы» (Connect). Real enrollment needs a one-time code generated in Business by an owner (a production write): do NOT try it. Instead tap the small bottom link «Посмотреть демо» / "View demo" (uz «Demoni ko‘rish»). The demo runs on fake local data (red strip «Демо · вымышленные данные»); payments inside it are fake and fine to complete. Demo PIN prompts: try 1234 then 0000. First screenshot the Connect screen itself (layout: tablets split into a black brand panel and a form; check the 6-digit code keypad and QR button, tap «Сканировать QR» only to see the permission/error, never grant a camera for scanning).

## Walk (demo): Sale (category, add 3 items, change quantity, remove one), Pay (methods, cash payment, paid screen), Orders list and an order, Tables, Shift/money screens (read only), Refund dialog (open, do not confirm), Hardware and Customer display settings (read only, no test print), More/settings. Judge tablet layout (space use, two-pane) vs phone. Language follows the device (ru/uz/en).

## Focus of this run (28.11): order change after a silent guest, hardware screen
1. In the demo open «Заказы» / Orders and the order №98. Below its lines there is a status card. It must read «Гость не ответил · решите сами» (uz «Mehmon javob bermadi · o‘zingiz hal qiling», en «No answer from the guest · your decision») in red, and under it a button «Оставить как было» / «Avvalgidek qoldirish» / «Keep as it was». Screenshot it. Tap the button once (demo only, nothing is sent). The status must change to «Гость не ответил — заказ без изменений» and the button must disappear. Report wrong texts, a missing button, a button that does nothing, or a cut/wrapped label as findings.
2. Open More/settings → «Оборудование» / Hardware (read only). Check the «Принтер по Bluetooth или USB» group and the «Принтер этикеток» group: labels fit, nothing cut, no raw keys. Do NOT press any test print.
