# Brief: Intop Staff — storekeeper, Canvas round 28.11 (demo)

Read AGENT_BRIEF.md first. Budget about 30 actions, report-first by action 30. Screenshot after every action.
DEBUG build in a local demo (launch arguments/extras set by the run): a pretend server inside the app answers every call; no sign-in; nothing leaves the phone; writes are refused locally ("demo_read_only" errors after a final action are expected — report them only if a screen breaks).
For every screen: report anything cut, overlapping, hidden under the bars, a word broken with a hyphen at a line end, a tap target under 44 pt (iOS) / 48 dp (Android), text in a wrong language, or a button that does nothing. Then check the expectations below and give PASS/FAIL with a screenshot for each.

Expectations:
1. Tabs «Приёмка / Пересчёт / Перемещения»; «Перемещения» has a number badge when incoming transfers wait.
2. «Перемещения» → segment «Входящие» keeps its badge also when selected.
3. «Приёмка»: status pill / «Принято к сведению» buttons have at least 44 pt / 48 dp touch.
4. «Пересчёт»: «Завершить пересчёт» pinned at the bottom.
