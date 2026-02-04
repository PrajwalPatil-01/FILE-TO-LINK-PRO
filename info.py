import re
import os
from os import environ, getenv
from Script import script

# --- Helper Functions ---
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "on"]:
        return True
    elif value.lower() in ["false", "no", "0", "off"]:
        return False
    return default

# =========================================================
# 🤖 BOT INFO & CREDENTIALS
# =========================================================
SESSION = environ.get('SESSION', 'Webavbot')
API_ID = int(environ.get('API_ID', '28690893'))
API_HASH = environ.get('API_HASH', 'c214f988aa1ac0b998ace0b7cd0e215f')
BOT_TOKEN = environ.get('BOT_TOKEN', '')

# Admin Settings
ADMINS = [int(x) for x in environ.get('ADMINS', '1454524346').split()]
OWNER_USERNAME = environ.get("OWNER_USERNAME", 'xp_prajwal')

# =========================================================
# 🗄️ DATABASE CONNECTION
# =========================================================
DB_URL = environ.get('DATABASE_URI', "mongodb+srv://FileToLinkBoT:FileToLinkBoT@cluster0.yijpbae.mongodb.net/?appName=Cluster0")
DB_NAME = environ.get('DATABASE_NAME', "Cluster0")

# =========================================================
# 📢 CHANNELS & LOGS
# =========================================================
# Mandatory Channels
BIN_CHANNEL = int(environ.get("BIN_CHANNEL", '-1003531139586'))
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", '-1003531139586'))

# Feature Specific Logs
PREMIUM_LOGS = int(environ.get("PREMIUM_LOGS", '-1003531139586'))
VERIFIED_LOG = int(environ.get('VERIFIED_LOG', '-1003531139586'))
SUPPORT_GROUP = int(environ.get("SUPPORT_GROUP", "-1003665059068"))

# Auth Channels (Safe Parsing)
auth_channel_str = environ.get("AUTH_CHANNEL", "-1003665059068")
AUTH_CHANNEL = [int(x) for x in auth_channel_str.split()] if auth_channel_str else []

# =========================================================
# 🔗 LINKS & URLS
# =========================================================
CHANNEL = environ.get('CHANNEL', 'https://t.me/TenxHubBackup')
SUPPORT = environ.get('SUPPORT', 'https://t.me/TenxHubBackup')
TUTORIAL_LINK_1 = environ.get('TUTORIAL_LINK_1', 'https://t.me/TenxHubBackup')
TUTORIAL_LINK_2 = environ.get('TUTORIAL_LINK_2', 'https://t.me/TenxHubBackup')

# =========================================================
# 🔐 VERIFICATION & SHORTENER
# =========================================================
IS_VERIFY = is_enabled(environ.get("IS_VERIFY", "True"), True)
IS_SECOND_VERIFY = is_enabled(environ.get("IS_SECOND_VERIFY", "False"), True)
IS_SHORTLINK = is_enabled(environ.get('IS_SHORTLINK', "True"), True)

# Verification Config
VERIFY_EXPIRE = int(environ.get('VERIFY_EXPIRE', 60)) # In Minutes/Hours based on logic
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'https://cuty.io')
SHORTLINK_API = environ.get('SHORTLINK_API', '0ba43bce4319bdae31dcea16542c69f97b6ffc62')

# Second Verification Config
SHORTLINK_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "https://cuty.io")
SHORTLINK_API2 = environ.get("SHORTENER_API2", "0ba43bce4319bdae31dcea16542c69f97b6ffc62")

# =========================================================
# ⚙️ SETTINGS & LIMITS
# =========================================================
FSUB = is_enabled(environ.get("FSUB", "True"), True)
ENABLE_LIMIT = is_enabled(environ.get("ENABLE_LIMIT", "True"), True)
MAINTENANCE_MODE = is_enabled(environ.get("MAINTENANCE_MODE", "False"), False)

# Time & Rate Limits
TIMEZONE = environ.get("TIMEZONE", "Asia/Kolkata")
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))
SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
RATE_LIMIT_TIMEOUT = int(environ.get("RATE_LIMIT_TIMEOUT", "600"))

# File Limits
MAX_FILES = int(environ.get("MAX_FILES", "5"))
BATCH_LIMIT = int(environ.get('BATCH_LIMIT', 60))

# =========================================================
# 🖼️ MEDIA & CAPTIONS
# =========================================================
QR_CODE = environ.get('QR_CODE', 'https://img.sanishtech.com/u/d1b5b187810c75d121b4acbf7ab6bde8.jpg')
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")
AUTH_PICS = environ.get('AUTH_PICS', 'https://ibb.co/8tDz8x0')
PICS = environ.get('PICS', 'https://ibb.co/8tDz8x0')
FILE_PIC = environ.get('FILE_PIC', 'https://ibb.co/SDrWNqjJ')

FILE_CAPTION = environ.get('FILE_CAPTION', script.CAPTION)

# =========================================================
# 🌐 SERVER & APP CONFIG
# =========================================================
WORKERS = int(getenv('WORKERS', '4'))
MULTI_CLIENT = False
name = str(environ.get('name', 'xpbotz'))

# Heroku & Port Config
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))
else:
    ON_HEROKU = False
    APP_NAME = None

PORT = int(getenv('PORT', '2626'))
NO_PORT = is_enabled(getenv("NO_PORT", "False"), False)
HAS_SSL = is_enabled(getenv("HAS_SSL", "False"), False)
BIND_ADDRESS = getenv("WEB_SERVER_BIND_ADDRESS", "127.0.0.1")

custom_url = environ.get("URL")
if custom_url:
    URL = custom_url
else:
    FQDN = getenv("FQDN", BIND_ADDRESS)
    PROTOCOL = "https" if HAS_SSL else "http"
    PORT_SEGMENT = "" if NO_PORT else f":{PORT}"
    URL = f"https://vague-maisie-prajwalpatil-332795f2.koyeb.app/"

# Default fallback if nothing works (Matches your provided koyeb link)
if not URL or URL == "/":
    URL = "https://vague-maisie-prajwalpatil-332795f2.koyeb.app/"
    
