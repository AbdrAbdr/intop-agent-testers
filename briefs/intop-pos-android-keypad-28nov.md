# Brief: Intop POS Android re-check: pay keypad with a large font (28.11)

Read AGENT_BRIEF.md first: its tools, rules and final report files all apply. Budget: about 20 actions; write report.md and findings.json early and update them. Screenshot after every action.

## Hard safety rules (production backend, test tenants only)
- NEVER pay with real data, enter card data, delete anything, change tenant or device settings, create enrollments, invite staff, or press print/test-print. Demo payments are fake and fine.
- Report text bugs as `TEXT[ru|uz|en]:` and layout bugs as `UI:` in findings.json. In report.md say for EACH check below: PASS or FAIL, with the screenshot number.

## Mode
On the Connect screen tap the small bottom link «Demoni ko‘rish» / «Посмотреть демо». Demo data is fake.

## Checks
1. Sale: add 2 dishes, open payment, cash. With the large system font the summary card (Buyurtma / Jami / Olindi / Qaytim) must be visible above the keypad. Type 200000: the «Qaytim» (change) line must be visible on screen without scrolling. Screenshot it.
2. Complete the fake cash payment and screenshot the paid screen.
3. «Buyurtmalar» → order №98: a red card «Mehmon javob bermadi · o‘zingiz hal qiling» and the button «Avvalgidek qoldirish». Screenshot it.
