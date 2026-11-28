# Brief: Intop Staff Android (waiter) — demo mode, no sign-in, nothing leaves the phone

Read AGENT_BRIEF.md first. Budget about 35 actions, report-first by action 35. Screenshot after every action.

This is a DEBUG build with a local demo: a pretend server inside the app answers every call; no account, no real tenant, writes are refused locally (an error like «demo_read_only» after a write is expected, not a bug).

## Start
1. Launch WITHOUT a shift: `adb shell am force-stop org.bytebit.intopstaff.dev; adb shell am start -n org.bytebit.intopstaff.dev/uz.intop.staff.MainActivity --es demo waiter --ez noshift true --ez intro true`
   - The permission steps appear first. Step «Не пропустите гостя» / «Mehmonni o‘tkazib yubormang»: are the title, text and the three example cards whole (not cut, nothing pushed off screen)? Can you reach «Позже / Keyinroq»? Go on; on «Ещё разрешения» is «Разрешить / Ruxsat» one line and tappable? Finish to the workspace (deny or allow system dialogs as you like). The steps appear only on this first launch.
   - Profile tab: is «Начать / Boshlash» a comfortable 48 dp tap target?
   - «Мои заказы» tab: the shift start screen; do NOT judge data.
2. Relaunch WITH a running shift: `adb shell am force-stop org.bytebit.intopstaff.dev; adb shell am start -n org.bytebit.intopstaff.dev/uz.intop.staff.MainActivity --es demo waiter`
   - «Мои заказы»: order cards; table badge = short number in the dark square, a long table name written in full next to it; segments «Заказы / Кухня» tall (~44 dp).
   - «Новый»: keypad; type 999 → the status under the number says there is no such table and the black bottom button stays grey; «C» clears. The «Гостей / Mehmonlar» card with − / + under the keypad; is it reachable (scroll) and not covered by the bottom button? Does the keypad jump when the screen finishes loading?
   - Profile → notification settings: scroll to the very bottom; the black «Отправить тестовое уведомление» and its hint fully visible above the bottom bar (you MAY press it: demo, nothing is sent; report what it says). «звук · сменить» rows tall enough to tap.
   - Profile → «Завершить / Yakunlash»: a dialog «Закончить смену?» with a line about open orders (copy its text) and BOTH buttons «Закончить смену» and «Отмена» visible. Press «Отмена» first (dialog closes, shift stays), then «Завершить» again → «Закончить смену» (demo refuses the write: a red reason must appear under the shift row in the profile — report its text).
Report every text in the phone language (`TEXT[uz]` / `TEXT[ru]`), cut/wrapped labels, buttons under 48 dp, anything under the bottom bar. In report.md list what you could not reach and why.
