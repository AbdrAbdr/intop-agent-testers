# Brief: Intop POS desktop with a customer screen on a second monitor

Read AGENT_BRIEF.md first, then briefs/intop-pos-desktop.md: its demo mode, tools, safety rules and report format apply unchanged
(`--demo`, no credentials, about 30 actions, never pay for real).

## Setup of this run
Linux Xvfb with two screens (`-screen 0 1920x1080 -screen 1 1280x800 +xinerama`): the cashier screen on the left, the second
(customer) screen to the right of it. The screenshot shows both side by side; click positions are in the same combined space, so a click on
the second screen has x = 1920 + its own x. The persona/prompt says if the second screen is missing.

## Mission
1. Open the till window on the first screen. Screenshot.
2. Find how the customer screen is opened (a menu or setting named like "Customer screen" / «Экран покупателя» / «Xaridor ekrani», or the app starts it with the role `customer`). Open it. It must appear on the SECOND screen, not on top of the till.
3. Ring up a demo sale: add 2-3 items, change a quantity, remove one. After each step look at the second screen: it must show the same cart lines and the total, update at once, and be non-interactive.
4. Start the payment step (demo only, do not confirm): the customer screen should show the amount to pay / the payment method state. Cancel back.
5. Close the customer screen from the till: the second screen must go back to idle/empty and the till must keep working.
Report as `UI:` / `TEXT[ru|uz|en]:`: customer screen on the wrong monitor, wrong or stale totals, clipped text at 1280x800, receipts of other languages than the till, controls that can be clicked on the customer screen, anything that differs when the screens have different resolutions.
In report.md say clearly whether a second screen was visible at all (if not, it is an environment limit: state what you saw).
