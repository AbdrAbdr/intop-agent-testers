# Brief: Intop POS desktop (Windows / macOS / Linux), demo walkthrough

Read AGENT_BRIEF.md first for the report format only: its phone tools do NOT apply here.
You drive a desktop app, the INTOP POS (cash register + waiter), already running in a
window on a real desktop (OS and screen size are in your task line). Tools, nothing else:
- See: `python scripts/desktop/screen.py results/<PERSONA> <NN>` (NN = 01, 02...). Read the PNG,
  then convert positions with the factor it prints (positions on the image x factor = click coordinates).
- `python scripts/desktop/click.py X Y [double|right]` - `python scripts/desktop/scroll.py X Y down|up [n]`
- `python scripts/desktop/key.py enter tab esc ctrl+a F11 ...` - `python scripts/desktop/type.py "text"` (click the field first)
- `python scripts/desktop/type_secret.py QA_NAME` only if a QA_* login is named in the task (not in demo).
Screenshot after EVERY action and look at it before the next. Budget: about 30 actions. Write report.md and findings.json NO LATER than action 30: if you are cut off before they exist, the whole run is lost. Skip steps rather than skip the report.
Write only under `results/<PERSONA>/`. `<PERSONA>` is in your task line (like `linux-dmitri`).

## Mode
The app runs in `--demo` mode: fake data, no server, no credentials, no network. If a PIN is
asked for staff sign-in, try `1234`. The language and theme are set by the launch flags; do not
change them except where a step below says so. NEVER touch real printers, cash drawers or payments:
printer settings are only OPENED and read (do not press print, test print or save).
Demo payments are fine to complete: they are fake and local.

## Walk through, in this order (screenshot each screen)
1. Login / staff sign-in, then the first screen. If a shift must be opened, open it (demo).
2. Sale: pick a category, add 3 items, change a quantity, open a line to edit it, remove one.
3. Pay: open payment, look at the methods, complete a cash payment, see the "paid" screen.
4. Orders: list, filters, open an order.
5. Shift: summary, close the shift screen only if it asks no real action (read it, go back).
6. Tables: hall plan, open a table, add a manual table if offered.
7. Waiter order: take an order for a table as a waiter, send it.
8. "More" menu: every entry once, then the receipt printer settings (read only).
9. Language: in "More" switch the language to the other two (ru, uz, en) one by one and look at
   the main screens again. Switch back at the end.

## Check on every screen
- Layout at THIS screen size (in the task line): is the window bigger than the screen, cut or
  overlapping text, buttons off-screen, unreadable contrast in this theme, tiny hit targets.
  Once, press F11 to toggle full screen and look again at the sale screen; press F11 again to go back.
- Text and translation: untranslated or mixed-language labels, raw keys (like `nav_group_hall`),
  wrong plurals or numbers, wrong currency format (the UI shows a word or symbol like "сум", never a
  code like "UZS"), the words "Hermes" or "Гермес" (must never appear). Report each as TEXT with
  the screen, the language and the exact text.
- Behaviour: keyboard focus, Tab and Enter work, Esc closes sheets, no frozen screen, crashes
  (screen.py says "app process: NOT RUNNING" if it died).
- Platform feel: the window title bar, shortcuts (copy and paste, F11), fonts that look wrong on THIS OS.

## Report
Format of AGENT_BRIEF.md (`report.md` + `findings.json`), but use `screen` names from the walk above
and prefix titles with `UI:` or `TEXT[ru|uz|en]:`. In report.md add: the OS and screen size,
which of the 9 steps you could NOT reach and why, and one line saying whether clicks and typing worked.
A later version of this brief may log in to the QA tenant; this one does not.
