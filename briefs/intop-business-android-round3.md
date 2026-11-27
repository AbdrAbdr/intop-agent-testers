# Brief: Intop Business Android — round 3: the quick-sections square and the dim (demo data)

Read AGENT_BRIEF.md first: its tools, rules and final report files all apply. Budget: about 30 actions. Screenshot after every action. The app starts in demo mode (no login). Read-only.

1. On Home, find the small handle (a short bar) right above the bottom tab bar. Tap it once. A square panel with section tiles opens above the tab bar.
   - Is the panel a card with rounded corners on all four sides? Does it look attached to the handle/tab bar, or does it float with an odd empty band? Measure the gap (px) between the panel's bottom edge and the handle.
   - Is the page behind the panel visibly dimmed (compare a card behind it before/after)? This must be clearly visible also in the dark theme.
   - Tap outside the panel: does it close?
2. Open the handle again and drag it up and down: does the panel follow the finger and settle open/closed?
3. Open «Ещё» / More → «Все разделы»: same checks for anything that opens from the bottom.
4. Top of each tab (Home, Orders, Menu, Analytics, More): from the bottom of the system status bar to the top of the title text, in px and in dp (state the screen density). Report the status bar height you measured.

## Report
AGENT_BRIEF.md format. report.md: answers 1–4 with PASS/FAIL and evidence; a table for 4. `UI:` prefix in findings.json. State device, size, density, theme and font scale.
