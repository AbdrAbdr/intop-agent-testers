# Brief: Intop Staff — hostess, Canvas round 28.11 (demo)

Read AGENT_BRIEF.md first. Budget about 30 actions, report-first by action 30. Screenshot after every action.
DEBUG build in a local demo (launch arguments/extras set by the run): a pretend server inside the app answers every call; no sign-in; nothing leaves the phone; writes are refused locally ("demo_read_only" errors after a final action are expected — report them only if a screen breaks).
For every screen: report anything cut, overlapping, hidden under the bars, a word broken with a hyphen at a line end, a tap target under 44 pt (iOS) / 48 dp (Android), text in a wrong language, or a button that does nothing. Then check the expectations below and give PASS/FAIL with a screenshot for each.

Expectations:
1. «Сегодня»: each booking shows the time and «до HH:MM»; actions «Пришли — посадить» + «Отменить» (late: «Не пришли»; new request: «Подтвердить» + «Отклонить»); a footnote «Брони с сайта, из Business и ваши — одна общая запись…».
2. Tap the stat tiles: «столов свободно» opens «Столы», «в очереди» opens «Очередь».
3. «Столы»: zone segments show free counts («Зал · 6»); tapping a table on cleaning opens a panel with «Убран — свободен».
4. Open a booking: phone shown masked like «+998 •• ••• 21 40»; «Позвонить» button; row «Гостей»; main action «Пришли — посадить за стол N».
5. «Очередь»: phones masked; «Позвали N мин назад — гостю ушло сообщение» on a called guest.
6. «+» new booking: −/+ guests are easy to tap; after «Создать бронь» a line «Бронь создана: …» (may be refused in demo — report what you see).
