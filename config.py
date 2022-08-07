## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgBQkqg-3wGgwlu6zI_b8DaBRI46hAZ7C8yXVWOufx3XEoDQQO1Asl_y6C18IZIx5f8WdNVNddtEYBty9U6Vy_lXUfYi7tWO-6lPP-zM2iDSmHlyyCAgZkOrGs0GnK2TLr5o6wL1xbBiNzqOvcX_Kd-3vqLwajsl9a_BX18BrSlT3uWOHjo5TCbmbDnLD6DV-0qaEjRBE_p5zskj_7ptpvCdrat0HsK9_2G8xtVxYFJpfqCFN4bwoDwyTrCjeAOeqFGYbSamNax9PmPQPsHnoq_VqBbWo-xF7PMiwZ5rpcY8E9zf5J8HmrHH4b_9JVy-MvcLs3AK_7nZPomOPQ1fo48dZIUbiAA")
BOT_TOKEN = getenv("BOT_TOKEN", "1743586001:AAGTH0MZqnXIQWKbaCxGI73WNwKoDdQwO0I")
BOT_NAME = getenv("BOT_NAME", "ميوزك")
API_ID = int(getenv("API_ID", "6440669"))
API_HASH = getenv("API_HASH", "fec788c7d1ccdfc9ec507b63818d0970")
OWNER_NAME = getenv("OWNER_NAME", "sofe")
OWNER_USERNAME = getenv("OWNER_USERNAME", "bc_cb")
ALIVE_NAME = getenv("ALIVE_NAME", "sofe")
BOT_USERNAME = getenv("BOT_USERNAME", "M51BoT")
OWNER_ID = getenv("OWNER_ID", "1686444936")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "bc_cb")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "no_nn")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "no_nn")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1686444936a").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
