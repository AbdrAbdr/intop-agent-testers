# Brief: Intop Business Android — round 4: the handle on the tab bar, the square, Day/Week/Month (demo data)

Read AGENT_BRIEF.md first: its tools, rules and final report files all apply. Budget: about 30 actions. Screenshot after every action. The app starts in demo mode (no login). Read-only.

## 1. The handle
On Home look at the small grey handle (36×4) right above the bottom tab bar. Zoom the screenshot: how many dp/px of gap between the handle and the tab bar's top edge? Does it read as part of the tab bar or as a separate strip?

## 2. Open the square
Tap the handle once. The quick-sections card opens over the page. Is there an EMPTY band at the bottom of the card (between the last row of tiles and the handle) taller than ~12 dp? Is the card resting on the handle (no big gap)?
Tap a tile in the LAST (bottom) row of the card: does that section open? (Write which.) Go back to Home.

## 3. Close it
Open the square again; tap the handle: does it close? Open again; drag the handle down slowly by about 2 cm: does it close?

## 4. Day / Week / Month
Read with the accessibility tree the bounds height of «День» / «Неделя» / «Месяц» (or UZ/EN words) in dp. Tap «Неделя»: is the selected pill visible and did the number change?

## Report
AGENT_BRIEF.md format. In report.md answer 1–4 with PASS / FAIL and evidence. `UI:` / `TEXT[ru|uz|en]:` prefixes in findings.json.
