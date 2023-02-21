import os
from os import getenv
from dotenv import load_dotenv
if os.path.exists("local.env"):
    load_dotenv("local.env")
API_ID = int(getenv("API_ID", "17885066")) #optional
API_HASH = getenv("API_HASH", "04d7683e84b08dc77feda1f10ac1c96a") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5106083511").split()))
OWNER_ID = int(getenv("OWNER_ID", "5106083511"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://alok_8709:alok_8709@cluster0.hl81hrq.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5844537792:AAFxR0hAQ-VdmLvEep1gbH2VnTYp0Yb1vz0")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/alok9523/LEGENDBOT-3/new/master")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "1BVtsOJ0Bu4jYNZfDKweDePDl_uTZrLUNxFDW20o5CPE0A9DCyXgi0sbleX9QP6tsVd94k6-5hgOZup2R6kuQZmZIs6bHn68yvNc1GtJJFghteqbPZeHyl295T2XjyVQd-Uv5HFor6f3cUeXJdmzEdYFY2iguxDWlzD3yUJ5vosdPXCx2WWVh0ECT46S8LXL9SQt9UvvcnfbmPajMB7Hb0Ly-63ZLaWPuazdM10lUyqu8_gwTFkz8xxE6dvjDpKGrF9DV5rwB7Y021_5smooEB9rEYW2YjB9Gj_5km52Gw7-krAKCtZ0cQZ62CjmVelO8EUtMs8MoVy97UlVpy2jjMg5NmaDIpDI=")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
