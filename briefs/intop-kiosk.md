# Brief: Intop Kiosk (self-order kiosk, tablet first)

Read AGENT_BRIEF.md first: its tools, rules and final report files all apply. Budget: about 30 actions, and report-first: write report.md and findings.json NO LATER than action 30 (draft them early, update at the end). Screenshot after every action.

## Hard safety rules (production backend, test tenants only)
- NEVER pay, enter card data, delete anything, change tenant or device settings, rotate PINs, create enrollments, invite staff, or press print/test-print. Reading a screen is fine.
- Never print or write credentials; write "the test password".
- Report text bugs as `TEXT[ru|uz|en]:` and layout/behaviour bugs as `UI:` in findings.json; also: untranslated or mixed labels, raw keys, cut-off text, wrong currency format (a word like "сум", never "UZS"), the words "Hermes"/"Гермес" (must never appear). Note the device type (phone or tablet) and whether the layout uses the space.
- In report.md list what you could NOT reach and why.

## Mode
Real enrollment is done from Business by scanning the kiosk's own QR (owner action, production write): do NOT do it. Two things are reachable:
1. If the app opened on «Подключите киоск» (K00): screenshot it, press «Показать код»/«Скрыть код» once, read the instruction text, check the QR and layout on this tablet. Do not scan or pair.
2. The run may have launched the debug demo already (menu with sample items; you will see the guest welcome/menu instead of K00). Then walk the guest flow: welcome and language chips (ru/uz/en), order type «Здесь / С собой», menu categories, a product with modifiers, cart, pay screen («На кассе»; fake, nothing is sent), order-number screen. Android only: you may relaunch other demo screens with `adb shell am start -S -n <package>/uz.intop.kiosk.MainActivity --es kioskDemo menu|product|cart|idle|stop|staff|start` (package = the installed id, e.g. org.bytebit.intopkiosk.dev; check with `adb shell pm list packages | grep intop`).
Both launches (normal and demo) are debug-only fake data. Kiosk is tablet-first: judge touch target size, text size from a distance, portrait vs landscape, idle reset. Hold the «Intop Kiosk» title 3 seconds opens the staff PIN screen: look at it, do not enter a PIN.

## Screen sizes and orientation (screen-size matrix)
The same app runs on many kiosk screens; the persona gives the size. Judge what you see against it:
- Big vertical kiosk (portrait 1080x1920 at ~240 dpi; Android personas `kiosk-portrait-*`, desktop `kiosk-1080x1920`): nothing clipped at the top or bottom, the whole menu and the cart/pay button reachable without scrolling the page, touch targets large (finger-sized), no tiny text.
- Landscape kiosk (1920x1080, `kiosk-landscape-1080p`, 10.1in tablet landscape): the menu uses the width (grid or two panes), no stretched phone column, the cart is visible.
- Small kiosk (7in tablet, desktop 1024x600): text still fits, categories and cart do not overlap.
- iPad mini, Air 11 and Pro 13, portrait and landscape (`ipad-*-landscape`): follow the orientations the app allows; if the app forces one orientation, say so instead of reporting it as a bug.
- Android: if the persona forces a display size, the prompt says so (`wm size`); the rotation is landscape when the persona says so. If the persona lists a role in the desktop matrix, the app is started with that role.
Report each size-specific difference as `UI:` with the size in the title.
