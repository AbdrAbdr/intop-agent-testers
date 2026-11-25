"""Builds the job matrix: one row per requested persona, with its device.
Env: PERSONAS (comma-separated ids, "all" for every persona of the platform, "none" or empty to skip it), PLATFORM (android | ios | desktop).
Desktop also reads OSES, RESOLUTIONS (comma-separated WxH: every persona runs at each, empty = the persona's own), LANG_OVERRIDE.
Mobile rows carry `ref` (the reference persona to compare with, "" for a reference persona itself) and `is_ref`.
Prints <platform>=<json> for $GITHUB_OUTPUT."""
import json, os

platform = os.environ.get("PLATFORM", "android")
wanted = [p.strip() for p in os.environ.get("PERSONAS", "").split(",") if p.strip()]
personas = {p["id"]: p for p in json.load(open("personas.json", encoding="utf-8"))}
if wanted == ["none"]:
    wanted = []
elif wanted == ["all"]:
    wanted = [pid for pid, p in personas.items() if p.get("platform") == platform]
missing = [p for p in wanted if p not in personas]
if missing:
    raise SystemExit(f"Unknown personas: {missing}")
other = [p for p in wanted if personas[p].get("platform", platform) != platform]
if other:  # its device settings would be silently replaced by defaults
    raise SystemExit(f"Not {platform} personas: {other}. Put them in the other platform's list.")
rows = []
if platform == "desktop":   # persona x OS x resolution; OSES = linux,windows,macos
    runners = {"linux": "ubuntu-latest", "windows": "windows-latest", "macos": "macos-15"}
    ress = [r.strip() for r in os.environ.get("RESOLUTIONS", "").split(",") if r.strip()]
    for os_name in [o.strip() for o in os.environ.get("OSES", "linux,windows,macos").split(",") if o.strip()]:
        for pid in wanted:
            d = personas[pid].get("device", {})
            for res in ress or [d.get("resolution", "1920x1080")]:
                rows.append({"persona": pid, "os": os_name, "runner": runners[os_name], "theme": d.get("theme", "light"),
                             "lang": os.environ.get("LANG_OVERRIDE") or personas[pid].get("locale", "en-US")[:2],
                             "resolution": res, "label": f"{pid}-{res}" if ress else pid,
                             "role": d.get("role", ""), "app_args": d.get("app_args", ""), "second_screen": d.get("second_screen", "")})
    wanted = []
for pid in wanted:
    p = personas[pid]
    d = p.get("device", {})
    geo = p.get("geo") or [48.8566, 2.3522]
    row = {"persona": pid, "theme": d.get("theme", "light"), "locale": p.get("locale", "en-US"),
           "geo": f"{geo[0]},{geo[1]}", "ref": p.get("ref", ""), "is_ref": "true" if p.get("reference") else "",
           "orientation": d.get("orientation", "portrait")}
    if platform == "ios":
        row.update({"simulator": d.get("simulator", "iPhone 16"), "ios": str(d.get("ios", "18")),
                    "text_size": d.get("text_size", "large")})
    else:
        row.update({"profile": d.get("profile", "pixel_6"), "api": d.get("android_api", 34),
                    "font_scale": str(d.get("font_scale", 1.0)), "device": d.get("name", "Pixel 6, Android 14"),
                    "wm_size": d.get("wm_size", ""), "wm_density": str(d.get("wm_density", "")),
                    "second_display": d.get("second_display", ""), "fold": d.get("fold", "")})
    rows.append(row)
print(f"{platform}=" + json.dumps(rows, ensure_ascii=False))
