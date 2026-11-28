# Brief: Intop Staff — waiter, Canvas round 28.11 (demo)

Read AGENT_BRIEF.md first. Budget about 30 actions, report-first by action 30. Screenshot after every action.
DEBUG build in a local demo (launch arguments/extras set by the run): a pretend server inside the app answers every call; no sign-in; nothing leaves the phone; writes are refused locally ("demo_read_only" errors after a final action are expected — report them only if a screen breaks).
For every screen: report anything cut, overlapping, hidden under the bars, a word broken with a hyphen at a line end, a tap target under 44 pt (iOS) / 48 dp (Android), text in a wrong language, or a button that does nothing. Then check the expectations below and give PASS/FAIL with a screenshot for each.

Expectations:
1. «Мои заказы»: segments «Заказы / Кухня / Бар»; a ready dish shows a small green number on «Кухня» (or «Бар»). An order whose guest asked for the bill shows a black chip «Счёт запрошен».
2. Open an order card → the bill sheet: next to «Пересадить» there is «Дозаказ»; it opens the menu of that table.
3. «Новый» tab: type 7 → «Свободен», button «Дальше · меню». Type 999 → «Такого стола нет в вашей смене».
4. Menu: if the menu has categories there are chips «Все / …» under the search; dishes with a photo show it on the left. Add a dish: the bottom button becomes «На кухню · 1 позиция · <сумма>» by itself after about a second — there is NO separate «Проверить заказ» step (it appears only after an error).
5. «Входящие»: the first button says what you do by kind («Иду», «Забираю», «Иду со счётом»); after it the second step says «Подошёл / Отнёс / Счёт отдал».
6. Profile → «Завершить» opens «Закончить смену?» with both lines: open orders AND «Вызовы гостей и задачи перестанут приходить». Press «Отмена».
