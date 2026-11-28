# Brief: Intop Staff — cashier, Canvas round 28.11 (demo)

Read AGENT_BRIEF.md first. Budget about 30 actions, report-first by action 30. Screenshot after every action.
DEBUG build in a local demo (launch arguments/extras set by the run): a pretend server inside the app answers every call; no sign-in; nothing leaves the phone; writes are refused locally ("demo_read_only" errors after a final action are expected — report them only if a screen breaks).
For every screen: report anything cut, overlapping, hidden under the bars, a word broken with a hyphen at a line end, a tap target under 44 pt (iOS) / 48 dp (Android), text in a wrong language, or a button that does nothing. Then check the expectations below and give PASS/FAIL with a screenshot for each.

Expectations:
1. «Заказы»: status chips «На кухне / Подано / Оплачен» (paid is green); segment «Просят счёт» without a « · N» counter; waiter chips filter the list.
2. Open an order: subtitle shows «N гостей» when known; block «Счёт» shows «Напечатать счёт для гостя» or a hint that no printer is set.
3. «Принять оплату» → cash: quick chips «Гость дал …» and «Без сдачи», change computed; after paying (may be refused in demo) a screen «Оплачено» with «К заказам».
4. «Смена»: rows Открыта / Продажи / Наличными / Картой и онлайн, «Должно быть в кассе», and a live «Расхождение» after typing the counted cash.
