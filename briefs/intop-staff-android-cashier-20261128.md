# Brief: Intop Staff Android (cashier) — orders board, demo mode

Read AGENT_BRIEF.md first. Budget about 20 actions, report-first by action 20. Screenshot after every action.
DEBUG build in a local demo (launch extras set by the run): a pretend server inside the app answers every call; no sign-in; nothing leaves the phone; writes are refused locally. The app opens as a cashier.

Report PASS/FAIL with a screenshot for each:
1. Open the orders board (tab «Заказы» / «Счета»). Nothing cut or overlapping.
2. The waiter chips row (initials in a circle + name): each chip is tappable and its touch area is at least 48 dp tall (report the measured bounds from the element list). Tap two chips: the list filters by that waiter.
3. On an order card the black button «Открыть счёт · …» is at least 48 dp tall; tap it and the bill opens; go back.
4. Anything cut, overlapping, or a tap target under 48 dp on these screens.
