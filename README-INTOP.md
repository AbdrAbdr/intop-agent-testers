# INTOP agent testers: how to start a pilot

AI testers drive the prebuilt INTOP Business apps on emulators/simulators against
production, as the owner of the **test** tenants only (Khan Chapan-test = FOOD,
Blackberry-test = MARKET). No INTOP source code lives here: builds are assets of the
GitHub Release `builds-20261125`, briefs are in `briefs/intop-business-*.md`.

Setup already done: results key pair (private key in `~/.mobile-agent-testers/`),
secrets `ARTIFACT_PASSPHRASE`, `ANTHROPIC_API_KEY` (set by the owner) and
`QA_{FOOD,MARKET}_OWNER_{EMAIL,PASSWORD}`. Briefs refer to the logins as
`$QA_FOOD_OWNER_EMAIL` etc.; the workflow passes them to the agent as env vars.

## Release assets (tag `builds-20261125`)

| Asset | App id |
|---|---|
| `business-android-debug-aifix.apk` | `org.bytebit.intopbussines.dev` (debug suffix `.dev`; talks to production `api.intop.uz`) |
| `intop-business-ios-sim.zip` (contains `IntopBusiness.app`) | `org.bytebit.intop-bussines` |
| `intop-pos-desktop-{windows,linux,macos}.jar.enc` | Intop POS desktop uber jars (Java 21), one per OS |

To refresh builds, build from a clean worktree of `origin/main`, then
`gh release upload builds-<date> <files> -R AbdrAbdr/intop-agent-testers` and use the new tag below.

## 1. Android pilot first (ubuntu, cheap)

```bash
gh workflow run agent-testers.yml -R AbdrAbdr/intop-agent-testers \
  -f app_dir=. -f framework=native -f app_id=org.bytebit.intopbussines.dev \
  -f android_build='bash scripts/fetch_build.sh business-android-debug-aifix.apk' \
  -f apk_path=business-android-debug-aifix.apk \
  -f android_personas=olga,grace -f ios_personas=none \
  -f brief=briefs/intop-business-food.md
```

MARKET: same command with `-f brief=briefs/intop-business-market.md`.
`olga` = Russian, dark; `grace` = English, 200% font. `ios_personas=none` skips macOS.
Add `-f model=haiku` to spend less, `-f record_video=true` for screen recordings.

## 2. iOS (macOS runner: expensive on a private repo)

```bash
gh workflow run agent-testers.yml -R AbdrAbdr/intop-agent-testers \
  -f app_dir=. -f framework=native -f app_id=org.bytebit.intop-bussines \
  -f ios_build='bash scripts/fetch_build.sh intop-business-ios-sim.zip' \
  -f ios_app_path=ios-app/IntopBusiness.app \
  -f android_personas=none -f ios_personas=aziz,noah \
  -f brief=briefs/intop-business-food.md
```

`aziz` = Uzbek (added to `personas.json`), `noah` = English, largest text size.
Android and iOS can run in one command (set both persona lists and both build inputs).

## 3. Collect results

```bash
gh run list -R AbdrAbdr/intop-agent-testers -L 3        # find the run id
cd /Users/abdr/intop-agent-testers && bash scripts/collect.sh <run id>
open runs/<run id>/SUMMARY.md                            # per persona: report.md, findings.json, screenshots
```

The decrypting key is read from `~/.mobile-agent-testers/AbdrAbdr_intop-agent-testers.pem`. Never commit `runs/`.

## Cost

- Model: needs the `ANTHROPIC_API_KEY` secret; roughly $0.15 to $0.55 per phone with sonnet on short walkthroughs, more with the 60-action briefs. `-f model=haiku` is cheaper.
- Actions minutes: the repo is private. Linux minutes use the free quota; **hosted macOS minutes count 10x**. Start with Android only, and run iOS with 1 or 2 personas.

## Moving iOS to a self-hosted Mac runner

Do this once, on the Mac that will host runs (this is NOT installed yet):

1. Get a registration token: `gh api -X POST repos/AbdrAbdr/intop-agent-testers/actions/runners/registration-token -q .token` (valid 1 hour; do not store it).
2. Install per GitHub's page https://github.com/AbdrAbdr/intop-agent-testers/settings/actions/runners/new (macOS, arm64): download and unpack the `actions-runner-osx-arm64` archive into a new folder outside any project, then
   `./config.sh --url https://github.com/AbdrAbdr/intop-agent-testers --token <token> --labels intop-mac --unattended` and `./svc.sh install && ./svc.sh start` (or `./run.sh` in a terminal for a one-off).
3. Switch the iOS jobs: `gh variable set IOS_RUNNER -b intop-mac -R AbdrAbdr/intop-agent-testers`. Back to hosted: `gh variable delete IOS_RUNNER -R AbdrAbdr/intop-agent-testers`.

Prerequisites on that Mac: Xcode, `gh`, Homebrew, Node, Python 3, and **passwordless sudo** for the
runner user: the iOS job runs `sudo xcode-select`, edits `/etc/hosts` and uses `pfctl` to block
analytics hosts. These edits persist on a self-hosted Mac (remove the `block_hosts` lines from
`/etc/hosts` afterwards). Jobs also create and boot their own simulators. Run `ios_personas` 1-2 at a time.


## Public repo
The repo is public so GitHub runners are free. Test builds are published only encrypted (`*.enc`, AES-256, key in the `BUILD_DECRYPT_KEY` secret) and decrypted inside the job by `scripts/fetch_build.sh`. Reports are encrypted with `results_public.pem`. Never commit INTOP source or credentials here.


## Desktop POS testers (Windows, macOS, Linux)

Workflow `desktop-testers.yml`: the POS uber jar of each OS (encrypted asset, decrypted by `scripts/fetch_build.sh`) is
launched `--window --demo` on a hosted runner (Linux under Xvfb + openbox, Windows, macOS 15) and driven by a Claude agent
through `scripts/desktop/{screen,click,key,scroll,type,type_secret}.py` (pyautogui + mss). Brief: `briefs/intop-pos-desktop.md`
(demo mode, no credentials, ~30 actions). Personas: `dmitri` (ru, 1366x768), `zarina` (uz, dark), `ethan` (en).

```bash
gh workflow run desktop-testers.yml -R AbdrAbdr/intop-agent-testers -f personas=dmitri            # 3 OS x 1 persona
gh workflow run desktop-testers.yml -R AbdrAbdr/intop-agent-testers -f personas=dmitri,zarina,ethan -f oses=linux
bash scripts/collect.sh <run id>      # same collect.sh; results land in runs/<id>/desktop-<os>-<persona>/
```

Linux runs at the persona's resolution; Windows and macOS hosted runners are fixed at 1024x768 (the 1440x900 window is
smaller than the app asks for, so expect layout findings). Rebuild the jars from a clean worktree of `origin/main`:
`./gradlew packageUberJarForCurrentOS -Pintop.target=windows-x64|linux-x64|macos-arm64` in `apps/Desktop/pos`, encrypt with
`openssl enc -aes-256-cbc -pbkdf2 -salt -pass file:<key>`, `gh release upload`. A later brief can log in to the QA tenant (`demo=false`).


## All native apps (Staff, POS, Kiosk, Display) - 2026-11-25

Assets of `builds-20261125`: `<app>-<android|ios>-0be683d.<apk|zip>.enc` for app = staff, pos, kiosk, display (debug Android builds with ids `org.bytebit.intop<app>.dev`; unsigned iOS Simulator builds, Debug config). Fetch with
`bash scripts/fetch_build.sh <app>-android-0be683d.apk` / `<app>-ios-0be683d.zip` (iOS app path `ios-app/Intop{Staff,POS,Kiosk,Display}.app`).
Briefs: `briefs/intop-{staff,pos,kiosk,display}.md`. New persona `dilnoza` (Android, uz).

- Staff: real e-mail login of the QA waiter/cook (`QA_STAFF_{WAITER,COOK}_{EMAIL,PASSWORD}`); no enrollment needed.
- POS: «Посмотреть демо» on the connect screen (fake data). Real enrollment needs a one-time code from Business (production write, not done).
- Kiosk, Display: cannot be enrolled without an owner action. New workflow input `launch_args` starts the debug demo: iOS `-kioskDemo menu -kioskLang uz` / `-displayDemo kitchen`; Android `--es kioskDemo menu` / `--es demo kitchen`. Without it only the connect screen is reachable.
- Builds are made on the maintainer's Mac (`gradlew :app:assembleDebug`, `xcodebuild -sdk iphonesimulator`, then `openssl enc` with the BUILD_DECRYPT_KEY key); nothing is run on that Mac.

**iOS builds must be ad-hoc signed.** Simulator builds made with `CODE_SIGNING_ALLOWED=NO` have no entitlements, so every Keychain write fails and sign-in shows "Could not keep the sign-in on this phone" / "Secure storage is unavailable" (seen in Staff and Business on 2026-11-25; not an app bug). Build with `CODE_SIGN_IDENTITY=- CODE_SIGNING_ALLOWED=YES CODE_SIGNING_REQUIRED=NO` (assets `staff-ios-0be683d`, `business-ios-0be683d` are signed; `pos/kiosk/display-ios-0be683d` are unsigned: fine for demo mode, rebuild signed before a real login).
Display brief: the button «Проверить принтер цеха» prints at once; two runs pressed it in demo mode before the brief said not to.


## Screen-size matrix with reference comparison (2026-11-25)

**Reference devices** (personas with `"reference": true`): `ref-iphone-17-pro-max`, `ref-ipad-pro-13-m4`, `ref-pixel-9-pro-xl`, `ref-pixel-tablet`. Every other mobile persona has `ref` (phones compare with the phone reference, tablets with the tablet one). iOS personas use the iOS 26 simulators (macos-15 has iOS 26.0-26.2 and every needed device type; iPhone 18 and iPhone Duo do not exist). Size spread: iPhone SE 3 / 13 mini / 17, iPad mini / Air 11 (+ landscape variants), small_phone, Pixel 7, Pixel 9 Pro Fold folded and unfolded (`fold`, set through `cmd device_state`, best effort), Nexus 7, 10.1in tablet, role screens `kiosk-*`, `tv-720p|1080p|4k` (display size forced with `wm size`/`wm density` on a tablet image, not an Android TV image), `pos-dual-display` (second display with `overlay_display_devices`). Languages ru, uz, en and large fonts are spread over them.

**Flow.** 1) Run the `ref-*` personas of one app. 2) `bash scripts/collect.sh <run>`. 3) `BUILD_KEY_FILE=<file with the BUILD_DECRYPT_KEY value> bash scripts/publish_reference.sh <run> <app slug>` packs the reference screenshots and `report.md`, encrypts them (AES-256, same key as the builds) and uploads `reference-<app>-<run>.tgz.enc` to the builds release. 4) Run the other personas with `-f reference_run=<run>`: each job downloads the asset (`scripts/fetch_reference.sh`), decrypts it on the runner only, and the agent gets `reference/<ref persona>/NN.png` plus `briefs/reference-compare.md` (compare each screen, report structural differences as bugs with both screenshot paths). Results stay encrypted as before; `reference/` is never uploaded.

```bash
# 1. reference run (FOOD example; for another app change app_id, builds, brief)
gh workflow run agent-testers.yml -R AbdrAbdr/intop-agent-testers -f app_dir=. -f framework=native \
  -f app_id=org.bytebit.intopbussines.dev -f android_build='bash scripts/fetch_build.sh business-android-df68766.apk' -f apk_path=business-android-df68766.apk \
  -f ios_build='bash scripts/fetch_build.sh business-ios-sim-df68766.zip' -f ios_app_path=ios-app/IntopBusiness.app \
  -f android_personas=ref-pixel-9-pro-xl,ref-pixel-tablet -f ios_personas=ref-iphone-17-pro-max,ref-ipad-pro-13-m4 -f brief=briefs/intop-business-food.md
# 2-3. bash scripts/collect.sh <run>; BUILD_KEY_FILE=... bash scripts/publish_reference.sh <run> business-food
# 4. the matrix (same inputs, other personas, plus -f reference_run=<run>)
```
Cost: `bash scripts/cost.sh <run>` (sums `total_cost_usd` after collect). Default model is sonnet; `-f model=haiku` is cheaper. Turn caps stay (80 mobile, 60 desktop).

**Desktop sizes.** `desktop-testers.yml` takes `resolutions` (comma list; each persona runs at each) and `extra_args`. Measured with `display-probe.yml`: Linux Xvfb any size (and two screens with `+xinerama`, persona `pos-dual`); Windows hosted runner switches to 1366x768 and 1920x1080 through `set_resolution.ps1` (2560x1440 is refused: the closest smaller size is used); macOS hosted runner is fixed to a list with a 1920x1080 maximum (no 1366x768, 1280x800 or 2560x1440): `set_resolution_macos.sh` picks the largest mode that fits inside the wanted size. The actual size is written to `results/<persona>/resolution.txt` and given to the agent. Role personas (`kiosk-*`, `board-*`, `ads-*`, `customer-*`, `pos-dual`) add `--role <role>`; the real flag names are pending in the app (`extra_args` covers changes).
