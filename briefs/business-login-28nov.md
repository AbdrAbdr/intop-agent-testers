# Brief: Intop Business iOS — sign-in focus on a small phone. Sign-in only, then READ-ONLY.

Read AGENT_BRIEF.md first. Budget: about 25 actions. Screenshot after EVERY action, before the next tap.
After signing in do nothing else: never create, change, send or pay anything.

## Steps (write exactly what you see)
1. Welcome → «У меня уже есть аккаунт» (scroll if needed). Screenshot.
2. Tap the e-mail field. Screenshot. Did the form move when the keyboard appeared? Where are the e-mail field, the password field and «Войти» now (y in pt)?
3. Type the e-mail with `type_secret.py QA_FOOD_OWNER_EMAIL`. Screenshot. Did anything move while typing?
4. Press the keyboard's Return / «Далее» key (do NOT tap the password field). Screenshot. Which field has the cursor now? Did the form scroll, and is «Войти» visible above the keyboard?
5. Type the password with `type_secret.py QA_FOOD_OWNER_PASSWORD`. Screenshot. Is it shown as dots in the password field? Is the e-mail field unchanged (no password text in it)? Never print either value.
6. Separately, if you can: tap «Назад»/close, open the sign-in again, tap the e-mail field, then tap the password field directly at the position you see in the LAST screenshot. Did the tap land in the password field?
7. Sign in (Return on the password, or «Войти»). Say whether you reached the app. Stop there.

## Report
AGENT_BRIEF.md format. A section per step with screenshot ids and positions. If no on-screen keyboard appears, say so and still answer steps 4–5 (Return can be sent as a key press).
