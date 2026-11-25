# Brief: Intop Business, FOOD owner walkthrough (Khan Chapan-test)

Read AGENT_BRIEF.md first: its tools, rules and final report files all apply.
This brief changes the mission and overrides two of its rules: you DO have a test
login (below), and the budget is about 60 actions instead of 30.

## App and account
Intop Business is the owner app of a FOOD (restaurant) business, a native app on the live
production server. You are the OWNER of the test business "Khan Chapan-test". It is a test
tenant with fake data. The app is already installed and open.

Login: the sign-in opens a secure browser page (Custom Tab on Android, a system
web-auth sheet on iOS; on iOS a system prompt "wants to use ... to sign in" is
expected: tap Continue). Choose the E-MAIL method. The credentials are in the
environment variables `$QA_FOOD_OWNER_EMAIL` and `$QA_FOOD_OWNER_PASSWORD`.
Type them through the shell so the value never appears in your own text, for example
`python3 scripts/android/type.py "$QA_FOOD_OWNER_EMAIL"` (or `scripts/ios/type.py` on iOS; tap the field first).
- Never print, echo, `cat`, or write these values anywhere: not in report.md, not in
  findings.json, not in any file. Write "the test password" instead.
- If the sign-in asks for something you do not have (SMS or e-mail code, OTP, captcha,
  Telegram, Google or Apple account), stop there. Do not try another account or
  method. Report it as a blocker with the screenshots, then test whatever you can
  reach without a login (the sign-in screen itself, language, layout, error texts
  for a wrong password: use a clearly wrong one such as `wrong-password-1`).
- If the business picker appears, pick "Khan Chapan-test".

## Hard safety rules (this is production, even if the data is fake)
- NEVER pay, never enter card data, never start a subscription or top-up.
- NEVER delete anything: orders, products, staff, branches, the business, the account.
  No "Delete", "Remove", "Disconnect", "Revoke", or "Log out everywhere".
- NEVER change tenant settings. Opening a settings screen and a toggle's detail is fine.
  If you changed something by accident, change it back at once and say so in the report.
- Do not invite staff, send messages to guests, or publish anything to the public site.
- Do not accept or reject real order-change proposals as a guest would; the only
  action allowed on a proposal is the one named below.

## Languages
The app has Russian, Uzbek and English. It follows the phone language. Write down every
text bug you see, in the language the screen is in: untranslated or mixed-language
labels, English text on a Russian or Uzbek screen, raw keys (like `nav_group_hall`),
cut-off or overlapping text, wrong plurals or numbers, wrong currency format
(the UI should show a word or symbol like "сум", not a code like "UZS"), the words
"Hermes" or "Гермес" (they must never appear). Report each as UI or TEXT bug with the
screen, the language and the exact text.

## Screens to cover
Spend the budget in this order. Screenshot after every action.
1. Sign-in and the first screen after it. Pick the business if asked.
2. Today / home: revenue and orders numbers, the oldest waiting order, branch switcher
   ("Business and branch" sheet), any readiness or tip cards. Pull to refresh once.
3. Orders list: filters or tabs, statuses, empty state, the source label of an order
   (Kiosk, App, Bot...). Open one order card: items, totals, guest, table, timeline.
4. Order-change proposal: an order card (or a banner on it) can show a pending proposal
   to the guest (replace or remove an item). If you find one, open it and look at its
   text and buttons. The ONLY action you may use is **«Отозвать»** (Withdraw /
   Qaytarib olish) and only on a proposal that is clearly a test one; it asks for
   confirmation first. If none exists, say so; do not create one.
5. Menu and stop-list: categories, a product card (photo, price, channels), the
   stop-list screen: how an item is stopped and the reason/time controls. Do not change
   availability; only open the screens and read them.
6. Staff and shifts: staff list and roles, the shift schedule, an open or closed shift
   summary. Read only.
7. "Ещё" / More menu: open the group «Зал и кухня» (Hall and kitchen: Hall / Kitchen /
   Kitchen display / Devices...) and its settings screens. Open each, read, go back.
   Do not toggle anything. Also look at the other groups once (Основное, Каталог,
   Продажи, Склад, Клиенты и маркетинг, Управление, Настройки).
8. Settings: language, notifications categories, appearance (light/dark), account.
   Do not change any value.

## What to report
Use the final report format of AGENT_BRIEF.md. In `findings.json`, give each issue a
`screen` from the list above and prefix its title with `UI:` (layout, taps, crash,
wrong state) or `TEXT:` (translation, wording). Mention the language of the screen in
the title, for example `TEXT[uz]: ...`. Also list, in report.md, which screens from the
list you could NOT reach and why (not available for this tenant, flag off, blocked).
