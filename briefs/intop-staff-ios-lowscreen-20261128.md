# Brief: Intop Staff iOS (waiter) — «Новый» step 1 on a small iPhone with large text, demo mode

Read AGENT_BRIEF.md first. Budget about 25 actions, report-first by action 25. Screenshot after every action.
DEBUG build in a local demo (launch arguments set by the run): a pretend server inside the app answers every call; no sign-in; nothing leaves the phone; writes are refused locally. The app opens on the waiter's «Новый» tab.

Expected layout for this text size (accessibility sizes): only the black bottom button is pinned; everything above it scrolls, and while you type a table number the number card comes back into view by itself.
Report PASS/FAIL with a screenshot for each:
1. On first view: the number card («Номер стола», the big number, the status line) is visible; nothing is cut or overlaps.
2. Scroll down: the WHOLE keypad including the last row «АБВ/C · 0 · ⌫» can be reached and tapped above the black button; nothing of the keypad stays hidden under the button.
3. Type 1, 0 (table 10): the number shows «10»; after each tap the number card is visible (it may scroll back into view); the 0 key was reachable.
4. Clear (⌫ or C), type 999: status «Такого стола нет в вашей смене», button grey, nothing jumps under your finger mid-typing (report if a key you were about to tap moved away).
5. The chips («Свободные» with 7, or «Недавние») and the «Гостей» card with − / + are reachable by scrolling; tap + and − once each.
6. Tap the chip «7» (if shown): step 2 «Шаг 2 из 2 · Стол 7 · N гостя» opens; go back with the arrow.
7. Anything cut, overlapping, or a tap target under 44 pt on this screen.
In report.md list what you could not reach and why.
