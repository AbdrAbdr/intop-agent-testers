# Brief: Intop Display (kitchen display / order boards, tablet first)

Read AGENT_BRIEF.md first: its tools, rules and final report files all apply. Budget: about 30 actions, and report-first: write report.md and findings.json NO LATER than action 30 (draft them early, update at the end). Screenshot after every action.

## Hard safety rules (production backend, test tenants only)
- NEVER pay, enter card data, delete anything, change tenant or device settings, rotate PINs, create enrollments, invite staff, or press print/test-print. Reading a screen is fine.
- Never print or write credentials; write "the test password".
- Report text bugs as `TEXT[ru|uz|en]:` and layout/behaviour bugs as `UI:` in findings.json; also: untranslated or mixed labels, raw keys, cut-off text, wrong currency format (a word like "сум", never "UZS"), the words "Hermes"/"Гермес" (must never appear). Note the device type (phone or tablet) and whether the layout uses the space.
- In report.md list what you could NOT reach and why.

## Mode
Real pairing needs a QR or claim code from Business (owner production write): do NOT pair. Reachable:
1. Normal launch: the Connect screen (text «Откройте Intop Business → Устройства → «Подключить экран»…», or «Подключение экранов Intop Display недоступно.»). Screenshot, read, check layout and language.
2. The run may have launched the debug demo (kitchen board with sample tickets). Then walk it: kitchen board (tickets, timers, colours), ready / «Вернуть последний», expo, ready-wall, issues and stop list, printer test (the button «Проверить принтер цеха» prints AT ONCE with no confirmation: NEVER press it, only look at it), manager PIN gate (demo PIN 0000 if asked). Android only: relaunch other demos with `adb shell am start -S -n <package>/uz.intop.display.MainActivity --es demo kitchen` (other values: see on-screen, e.g. pin, expo; extras `--es theme dark`). Check the package with `adb shell pm list packages | grep intop`.
Display is a wall/kitchen screen: judge legibility from a distance, density, orientation (iPad is landscape only), burn-in-safe dark theme, language ru/uz/en.

## Screen sizes and orientation (screen-size matrix)
The screen role comes from the persona. Judge legibility from a distance (about 3 m) on every size:
- TV 1080p (`tv-1080p`, desktop `board-1920x1080`, `ads-1920x1080`), TV 4K (`tv-4k`, desktop `board-3840x2160`) and TV 720p (`tv-720p`): headings and ticket text readable, not tiny at 4K and not wrapped or cut at 720p, ticket columns fill the screen, nothing under the system bars.
- Large tablet in landscape (10.1in, `tablet-101-landscape`) and small 7in (`tablet-7in-landscape`): the board uses the width, no phone-style single column.
- iPad mini, Air 11 and Pro 13 (`ipad-*-landscape`): Display is landscape only; in portrait it must either stay landscape or show a clear message, never a broken layout.
- Desktop role boards (`--role board`, `--role ads`): same checks; the ads role must not show controls.
Report each size-specific difference as `UI:` with the size in the title.
