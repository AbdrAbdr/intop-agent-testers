# Brief: Intop POS (Android) with a customer-facing second display

Read AGENT_BRIEF.md and briefs/intop-pos.md first: demo mode, safety rules and report format apply unchanged.

The emulator has a second (overlay) display attached for the customer screen (the app shows it through Android's Presentation API: cart and total, non-interactive).
- Find its id: `adb shell dumpsys SurfaceFlinger --display-id` (a second id is listed) or `adb shell dumpsys display | grep -E "mDisplayId|FLAG_PRESENTATION|overlay"`.
- Capture it: `adb exec-out screencap -d <display id> -p > results/<persona>/NNb.png`, and look at it with Read.
Mission: open the POS demo, ring up 2-3 items, change a quantity, remove one, start the payment step (do not confirm). After each step capture the second display: it must show the same cart lines and total, update at once and not be interactive. Report mismatches, clipped text, wrong language, a customer screen that never appears (say if the display was visible to the app: `adb shell dumpsys display | grep -i presentation`), as `UI:`.
