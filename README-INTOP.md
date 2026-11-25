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
