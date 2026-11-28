# Brief: Intop Business — sign-in screen with the keyboard (Khan Chapan-test). Sign-in only.

Read AGENT_BRIEF.md first. Budget: about 25 actions. Screenshot after every action. After signing in stop; change nothing.

1. Welcome → «У меня уже есть аккаунт» (uz «Menda hisob bor»). Screenshot.
2. Tap the e-mail field. With the keyboard up: is the close «×» fully visible below the status bar (not cut by the clock)? Is the heading «С возвращением» / «Qaytganingizdan xursandmiz» drawn under the clock at any point? Screenshot.
3. Type the e-mail (`type_secret.py QA_FOOD_OWNER_EMAIL`). Press Return / Next. Which field has the cursor? Is the whole password field visible above the sign-in button? Screenshot.
4. Type the password (`type_secret.py QA_FOOD_OWNER_PASSWORD`, dots expected). Tap the sign-in button once. Did the first tap sign in?
5. On Home (Android only): the «Hisobni chop etish» pill on a table order — skip this; stop after sign-in.
Report y-positions, yes/no answers and screenshot ids.
