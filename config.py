from os import getenv
from dotenv import load_dotenv

load_dotenv()


SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))

class Config:
    BOT_TOKEN =os.environ.get("BOT_TOKEN",None) # 🌚 get it from @botfather (telegram) by sending /newbot command.
    API_ID = int(os.environ.get("API_ID",None)) # 🌚 Same as APP_ID. Get it from my.telegram.org.
    API_HASH = os.environ.get("API_HASH",None) # 🌚 Get it from my.telegram.org.
    
