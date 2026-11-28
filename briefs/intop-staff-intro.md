# Brief: Intop Staff iOS — first-launch steps, word breaks (demo)

Read AGENT_BRIEF.md first. Budget about 30 actions, report-first by action 30. Screenshot after every action.
DEBUG build in a local demo (launch arguments/extras set by the run): a pretend server inside the app answers every call; no sign-in; nothing leaves the phone; writes are refused locally ("demo_read_only" errors after a final action are expected — report them only if a screen breaks).
For every screen: report anything cut, overlapping, hidden under the bars, a word broken with a hyphen at a line end, a tap target under 44 pt (iOS) / 48 dp (Android), text in a wrong language, or a button that does nothing. Then check the expectations below and give PASS/FAIL with a screenshot for each.

Do NOT accept the system permission dialogs; use «Позже» / «Дальше».
Expectations:
1. Every grey paragraph is readable (not a black box) and no Russian word is split with a hyphen at a line end — quote any split word.
2. On every step the buttons stay visible at the bottom without scrolling; the step's content scrolls above them; each step opens from its top.
