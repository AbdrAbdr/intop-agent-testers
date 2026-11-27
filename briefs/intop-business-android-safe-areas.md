# Brief: Intop Business Android — gaps at the status bar and the navigation bar (demo data)

Read AGENT_BRIEF.md first: its tools, rules and final report files all apply. Budget: about 35 actions. Screenshot after every action.

The app starts in demo mode with sample data: no login. Read-only: never tap anything that sends, saves, pays or deletes.

## What to measure on every screen
The owner says the gap between the system status bar (clock, battery) and the app's header looks too big, and the same at the bottom above the system navigation (gesture line or buttons). Reference: Telegram — the header starts right under the status bar, the bottom tab bar sits right on the navigation area.

For each screen below, from the screenshot and the UI tree (bounds), write in px of the screenshot:
- **Top gap**: from the bottom of the status bar to the top of the first app content (title or header row). Note whether the empty band looks bigger than a normal one-line margin.
- **Bottom gap**: from the bottom of the app's tab bar / last button to the top of the system navigation area. Note any empty band, or any content hidden behind the navigation.
- Anything cut off, overlapping the status bar or the navigation, or text truncated.

## Screens
1. Home («Главная» / Home) right after launch.
2. Orders tab; then open the first order (detail screen); then go back.
3. Menu tab.
4. Analytics tab.
5. «Ещё» / More tab; open «Касса и смены» / Cash and shifts; go back.
6. Open any bottom sheet you can open without changing data (e.g. a filter or period picker) and measure its bottom edge against the navigation; close it.

## Report
AGENT_BRIEF.md format. In report.md a table: screen | top gap px | bottom gap px | looks right? (yes/no + why). Then findings. `UI:` prefix in findings.json for layout issues. State the device, screen size and font scale you ran on.
