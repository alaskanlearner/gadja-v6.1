from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ Perintah Untuk Pengguna Bot MAS GACOR RESMI
 ├ /start - Memulai Bot
 ├ /about - Informasi Tentang Bot
 ├ /help - Bantuan Pengguna
 └ /id - Cek Id Akun Anda

👩‍💻 VIP Gratis : <a href='https://bit.ly/gacolersmisi'>Bot_Promo</a>\n
👨‍💻 Asupan Gratis: </b><a href='https://t.me/gacolers_portal'>@gacolers_portal</a>
"""

    close = [
        [InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ", callback_data="about"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    ABOUT = """
<b><i><u>Identitas Bot KONSUMSI BERSAMA</u></i>\n

@{} adalah <u>Layanan Bot Asupan</u> Untuk Para Gacolers Indonesia. Bot Memiliki Banyak Asupan dari Lokal Hingga Mancanegara.\n

<i><u>Apa Itu Gacolers?</u></i>
Gacolers adalah Sebutan Untuk Member dan Penikmat Asupan Mas Gacor dari Indonesia dan Sekitarnya.\n

<i>Info Selengkapnya:</i>
 • Admin : @{}
 • Channel Backup : <a href='https://t.me/gacolers_channel'>@gacolers_channel</a>
 • Bot Support Centre : <a href='https://bit.ly/gacolersmngc'>@Bot_Kendala</a>\n

👩‍💻 VIP Gratis : <a href='https://bit.ly/gacolersmisi'>Bot_Promo</a>\n
👨‍💻 Asupan Gratis : </b><a href='https://t.me/gacolers_portal'>@gacolers_portal</a>
<i>by ©Mas Gacor Resmi</i>.\n\n
"""