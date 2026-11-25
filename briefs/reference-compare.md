# Reference comparison (read when the prompt says REFERENCE RUN or REFERENCE COMPARISON)

The owner fixed reference devices: iPhone 17 Pro Max, iPad Pro 13 M4, Pixel 9 Pro XL, Pixel Tablet.
On every other screen size the app must look like it does on the reference: the same structure, nothing clipped
or overlapping, no stretched phone layout on a tablet. Only the same device class is compared (phone with phone,
tablet with tablet).

## Reference run
- Do the brief's flow once, methodically. Take a screenshot of every distinct screen and state (each tab, each
  dialog, empty and filled lists, errors you can reach). Do not skip screens to save actions.
- In report.md add a section "Screens": one line per screenshot, `NN: <screen title>, <what is on it>`.
  Other devices are compared against these screenshots by their number.

## Comparison
- The reference screenshots are `reference/<reference persona>/NN.png`, with `report.md` listing what each shows.
  Look at them with Read. They are private test data: never copy them into results, never describe credentials.
- Compare every screen with the reference screenshot of the same screen; report any structural difference
  (clipped text, hidden controls, stretched or squeezed layout, different navigation) as a bug with both
  screenshot paths: yours (`results/<persona>/NN.png`) and the reference (`reference/<reference persona>/NN.png`).
- Differences that are only expected for the device (a narrower column that wraps, a second pane that appears on a
  tablet) are not bugs: say so in one line. A phone layout stretched across a tablet, or a tablet layout squeezed
  on a phone, is a bug.
- In findings.json start the title with `[layout vs reference]`, keep your numbers in `screens`, and add `"reference_screens": ["reference/<reference persona>/NN.png"]`.
- If a reference screen has no counterpart, or the reference lacks the screen you reached, say so instead of guessing.
