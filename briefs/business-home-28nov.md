# Brief: Intop Business — Home layout and touch sizes (Khan Chapan-test). READ-ONLY after sign-in.

Read AGENT_BRIEF.md first. Budget: about 30 actions. Screenshot after every action. Never create, change, send or pay anything.

1. Sign in (Welcome → «Menda hisob bor» / «У меня уже есть аккаунт»; `type_secret.py QA_FOOD_OWNER_EMAIL`, Return, `type_secret.py QA_FOOD_OWNER_PASSWORD`). Before typing: is the link «Hisobingiz yo‘qmi? Biznes yaratish» / «Нет аккаунта? Создать бизнес» at the bottom fully visible, not cut by the screen edge? Pick «Khan Chapan-test», skip the intro.
2. Home: sizes of the period switch «Kun / Hafta / Oy» from the accessibility list (each width × height). Are all at least 44 × 44 pt / 48 dp?
3. Home: the three stat tiles («Buyurtmalar», «Jarayonda va tayyor», «O‘rt. chek»): are they the same height?
4. Home: scroll to the very bottom. Can every card's text be read above the floating tab bar at the end of the scroll?
5. iOS only: the last tab of the bottom bar — its visible label and its accessibility name. Are they the same?
6. Android only: the hint «Barcha bo‘limlar — tutqich ostida»: while it shows, can you read all four «Tezkor amallar» tiles by scrolling, without closing the hint?
Report sizes, yes/no answers and screenshot ids.
