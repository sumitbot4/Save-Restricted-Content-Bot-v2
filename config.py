# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "24219567")
API_HASH = getenv("API_HASH", "d2b068e63ff5c51ff397dd500d0d51b6")
BOT_TOKEN = getenv("BOT_TOKEN", "7929128384:AAFr0Obdr5EbQTFw7ZdXb7chVl1Vo46CrB4")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6442268649").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://cosmicpower6:xfc5FG8D5ySEKnxo@cluster0.hpq7svo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "4986532847")
CHANNEL_ID = int(getenv("CHANNEL_ID", "1002859357880"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "5000"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
