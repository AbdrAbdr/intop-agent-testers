# Brief: Intop Staff — cook, Canvas round 28.11 (demo)

Read AGENT_BRIEF.md first. Budget about 30 actions, report-first by action 30. Screenshot after every action.
DEBUG build in a local demo (launch arguments/extras set by the run): a pretend server inside the app answers every call; no sign-in; nothing leaves the phone; writes are refused locally ("demo_read_only" errors after a final action are expected — report them only if a screen breaks).
For every screen: report anything cut, overlapping, hidden under the bars, a word broken with a hyphen at a line end, a tap target under 44 pt (iOS) / 48 dp (Android), text in a wrong language, or a button that does nothing. Then check the expectations below and give PASS/FAIL with a screenshot for each.

Expectations:
1. Kitchen screen: segments with counts; one action per ticket («Начать готовить / Готово / Выдано»).
2. On a dish → «Проблема» / «Не могу приготовить»: the comment field shows a hint «Например: закончилась баранина, будет к 19:00»; the note under the form says «Позиция встанет на паузу до решения менеджера. Заказ целиком не отменяется, деньги и склад кухня не трогает.» Close without sending.
