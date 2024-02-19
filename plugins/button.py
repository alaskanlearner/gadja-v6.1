# last update : 10:08 AM 12/11/2023
from config import(
    FORCE_SUB_1,
    FORCE_SUB_2,
    FORCE_SUB_3,
    FORCE_SUB_4
)
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if (
        not FORCE_SUB_1
        and not FORCE_SUB_2
        and not FORCE_SUB_3
        and not FORCE_SUB_4
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ᴛᴜᴛᴜᴘ", 
                    callback_data="close"
                ),
            ],
        ]
        return buttons
    if (
        FORCE_SUB_1
        and not FORCE_SUB_2
        and not FORCE_SUB_3
        and not FORCE_SUB_4
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="ᴄʜᴀɴɴᴇʟ", 
                    url=client.invitelink
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ᴛᴜᴛᴜᴘ", 
                    callback_data="close"
                ),
            ],
        ]
        return buttons
    if (
        FORCE_SUB_2
        and not FORCE_SUB_1
        and not FORCE_SUB_3
        and not FORCE_SUB_4
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="ᴄʜᴀɴɴᴇʟ", 
                    url=client.invitelink2
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ᴛᴜᴛᴜᴘ", 
                    callback_data="close"
                ),
            ],
        ]
        return buttons
    if (
        FORCE_SUB_3
        and not FORCE_SUB_1
        and not FORCE_SUB_2
        and not FORCE_SUB_4
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="ᴄʜᴀɴɴᴇʟ", 
                    url=client.invitelink3
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ᴛᴜᴛᴜᴘ", 
                    callback_data="close"
                ),
            ],
        ]
        return buttons
    if (
        FORCE_SUB_4
        and not FORCE_SUB_1
        and not FORCE_SUB_2
        and not FORCE_SUB_3
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="ᴄʜᴀɴɴᴇʟ", 
                    url=client.invitelink4
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ᴛᴜᴛᴜᴘ", 
                    callback_data="close"
                ),
            ],
        ]
        return buttons
    if (
        FORCE_SUB_1
        and FORCE_SUB_2
        and not FORCE_SUB_3
        and not FORCE_SUB_4
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="ᴄʜᴀɴɴᴇʟ", 
                    url=client.invitelink1
                ),
                InlineKeyboardButton(
                    text="ᴄʜᴀɴɴᴇʟ", 
                    url=client.invitelink2
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ᴛᴜᴛᴜᴘ", 
                    callback_data="close"
                ),
            ],
        ]
        return buttons
    if (
        FORCE_SUB_1
        and FORCE_SUB_3
        and not FORCE_SUB_2
        and not FORCE_SUB_4
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="ᴄʜᴀɴɴᴇʟ", 
                    url=client.invitelink
                ),
                InlineKeyboardButton(
                    text="ᴄʜᴀɴɴᴇʟ", 
                    url=client.invitelink3
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ᴛᴜᴛᴜᴘ", 
                    callback_data="close"
                ),
            ],
        ]
        return buttons
    if (
        FORCE_SUB_1
        and FORCE_SUB_4
        and not FORCE_SUB_2
        and not FORCE_SUB_3
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="ᴄʜᴀɴɴᴇʟ", 
                    url=client.invitelink1
                ),
                InlineKeyboardButton(
                    text="ᴄʜᴀɴɴᴇʟ", 
                    url=client.invitelink4
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ᴛᴜᴛᴜᴘ", 
                    callback_data="close"
                ),
            ],
        ]
        return buttons
    if (
        FORCE_SUB_2
        and FORCE_SUB_3
        and not FORCE_SUB_1
        and not FORCE_SUB_4
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="ᴄʜᴀɴɴᴇʟ", 
                    url=client.invitelink2
                ),
                InlineKeyboardButton(
                    text="ᴄʜᴀɴɴᴇʟ", 
                    url=client.invitelink3
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ᴛᴜᴛᴜᴘ", 
                    callback_data="close"
                ),
            ],
        ]
        return buttons
    if (
        FORCE_SUB_2
        and FORCE_SUB_4
        and not FORCE_SUB_1
        and not FORCE_SUB_3
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="ᴄʜᴀɴɴᴇʟ", 
                    url=client.invitelink2
                ),
                InlineKeyboardButton(
                    text="ᴄʜᴀɴɴᴇʟ", 
                    url=client.invitelink4
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ᴛᴜᴛᴜᴘ", 
                    callback_data="close"
                ),
            ],
        ]
        return buttons
    if (
        FORCE_SUB_3
        and FORCE_SUB_4
        and not FORCE_SUB_1
        and not FORCE_SUB_2
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="ᴄʜᴀɴɴᴇʟ", 
                    url=client.invitelink3
                ),
                InlineKeyboardButton(
                    text="ᴄʜᴀɴɴᴇʟ", 
                    url=client.invitelink4
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ᴛᴜᴛᴜᴘ", 
                    callback_data="close"
                ),
            ],
        ]
        return buttons
    if (
        FORCE_SUB_1
        and FORCE_SUB_2
        and FORCE_SUB_3
        and not FORCE_SUB_4
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="ᴄʜᴀɴɴᴇʟ", 
                    url=client.invitelink
                ),
                InlineKeyboardButton(
                    text="ᴄʜᴀɴɴᴇʟ", 
                    url=client.invitelink2
                ),
                InlineKeyboardButton(
                    text="ᴄʜᴀɴɴᴇʟ", 
                    url=client.invitelink3
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ᴛᴜᴛᴜᴘ", 
                    callback_data="close"
                ),
            ],
        ]
        return buttons
    if (
        FORCE_SUB_1
        and FORCE_SUB_2
        and FORCE_SUB_4
        and not FORCE_SUB_3
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="ᴄʜᴀɴɴᴇʟ", 
                    url=client.invitelink
                ),
                InlineKeyboardButton(
                    text="ᴄʜᴀɴɴᴇʟ", 
                    url=client.invitelink2
                ),
                InlineKeyboardButton(
                    text="ᴄʜᴀɴɴᴇʟ", 
                    url=client.invitelink4
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ᴛᴜᴛᴜᴘ", 
                    callback_data="close"
                ),
            ],
        ]
        return buttons
    if (
        FORCE_SUB_1
        and FORCE_SUB_3
        and FORCE_SUB_4
        and not FORCE_SUB_2
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="ᴄʜᴀɴɴᴇʟ", 
                    url=client.invitelink
                ),
                InlineKeyboardButton(
                    text="ᴄʜᴀɴɴᴇʟ", 
                    url=client.invitelink3
                ),
                InlineKeyboardButton(
                    text="ᴄʜᴀɴɴᴇʟ", 
                    url=client.invitelink4
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ᴛᴜᴛᴜᴘ", 
                    callback_data="close"
                ),
            ],
        ]
        return buttons
    if (
        FORCE_SUB_2
        and FORCE_SUB_3
        and FORCE_SUB_4
        and not FORCE_SUB_1
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="ᴄʜᴀɴɴᴇʟ", 
                    url=client.invitelink2
                ),
                InlineKeyboardButton(
                    text="ᴄʜᴀɴɴᴇʟ", 
                    url=client.invitelink3
                ),
                InlineKeyboardButton(
                    text="ᴄʜᴀɴɴᴇʟ", 
                    url=client.invitelink4
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ᴛᴜᴛᴜᴘ", 
                    callback_data="close"
                ),
            ],
        ]
        return buttons
    if (
        FORCE_SUB_1
        and FORCE_SUB_2
        and FORCE_SUB_3
        and not FORCE_SUB_4
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="ᴄʜᴀɴɴᴇʟ", 
                    url=client.invitelink1
                ),
                InlineKeyboardButton(
                    text="ᴄʜᴀɴɴᴇʟ", 
                    url=client.invitelink2
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ᴄʜᴀɴɴᴇʟ", 
                    url=client.invitelink3
                ),
                InlineKeyboardButton(
                    text="ɢʀᴏᴜᴘ", 
                    url=client.invitelink4
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ᴛᴜᴛᴜᴘ", 
                    callback_data="close"
                ),
            ],
        ]
        return buttons
    

def fsub_button(client, message):
    if (
        FORCE_SUB_1
        and not FORCE_SUB_2
        and not FORCE_SUB_3
        and not FORCE_SUB_4
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="ᴊᴏɪɴ ᴅᴜʟᴜ", 
                    url=client.invitelink
                ),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if (
        FORCE_SUB_2
        and not FORCE_SUB_1
        and not FORCE_SUB_3
        and not FORCE_SUB_4
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="ᴊᴏɪɴ ᴅᴜʟᴜ", 
                    url=client.invitelink2
                ),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if (
        FORCE_SUB_3
        and not FORCE_SUB_1
        and not FORCE_SUB_2
        and not FORCE_SUB_4
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="ᴊᴏɪɴ ᴅᴜʟᴜ", 
                    url=client.invitelink3
                ),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if (
        FORCE_SUB_4
        and not FORCE_SUB_1
        and not FORCE_SUB_2
        and not FORCE_SUB_3
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="ᴊᴏɪɴ ᴅᴜʟᴜ", 
                    url=client.invitelink4
                ),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if (
        FORCE_SUB_1
        and FORCE_SUB_2
        and not FORCE_SUB_3
        and not FORCE_SUB_4
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="ᴊᴏɪɴ ᴅᴜʟᴜ", 
                    url=client.invitelink
                ),
                InlineKeyboardButton(
                    text="ᴊᴏɪɴ ᴅᴜʟᴜ", 
                    url=client.invitelink2
                ),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if (
        FORCE_SUB_1
        and FORCE_SUB_3
        and not FORCE_SUB_2
        and not FORCE_SUB_4
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="ᴊᴏɪɴ ᴅᴜʟᴜ", 
                    url=client.invitelink
                ),
                InlineKeyboardButton(
                    text="ᴊᴏɪɴ ᴅᴜʟᴜ", 
                    url=client.invitelink3
                ),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if (
        FORCE_SUB_1
        and FORCE_SUB_4
        and not FORCE_SUB_2
        and not FORCE_SUB_3
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="ᴊᴏɪɴ ᴅᴜʟᴜ", 
                    url=client.invitelink
                ),
                InlineKeyboardButton(
                    text="ᴊᴏɪɴ ᴅᴜʟᴜ", 
                    url=client.invitelink4
                ),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if (
        FORCE_SUB_2
        and FORCE_SUB_3
        and not FORCE_SUB_1
        and not FORCE_SUB_4
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="ᴊᴏɪɴ ᴅᴜʟᴜ", 
                    url=client.invitelink2
                ),
                InlineKeyboardButton(
                    text="ᴊᴏɪɴ ᴅᴜʟᴜ", 
                    url=client.invitelink3
                ),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if (
        FORCE_SUB_2
        and FORCE_SUB_4
        and not FORCE_SUB_1
        and not FORCE_SUB_3
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="ᴊᴏɪɴ ᴅᴜʟᴜ", 
                    url=client.invitelink2
                ),
                InlineKeyboardButton(
                    text="ᴊᴏɪɴ ᴅᴜʟᴜ", 
                    url=client.invitelink4
                ),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if (
        FORCE_SUB_3
        and FORCE_SUB_4
        and not FORCE_SUB_1
        and not FORCE_SUB_2
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="ᴊᴏɪɴ ᴅᴜʟᴜ", 
                    url=client.invitelink3
                ),
                InlineKeyboardButton(
                    text="ᴊᴏɪɴ ᴅᴜʟᴜ", 
                    url=client.invitelink4
                ),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if (
        FORCE_SUB_1
        and FORCE_SUB_2
        and FORCE_SUB_3
        and not FORCE_SUB_4
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="ᴊᴏɪɴ ᴅᴜʟᴜ", 
                    url=client.invitelink
                ),
                InlineKeyboardButton(
                    text="ᴊᴏɪɴ ᴅᴜʟᴜ", 
                    url=client.invitelink2
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ᴊᴏɪɴ ᴅᴜʟᴜ", 
                    url=client.invitelink3
                ),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if (
        FORCE_SUB_1
        and FORCE_SUB_2
        and FORCE_SUB_4
        and not FORCE_SUB_3
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="ᴊᴏɪɴ ᴅᴜʟᴜ", 
                    url=client.invitelink
                ),
                InlineKeyboardButton(
                    text="ᴊᴏɪɴ ᴅᴜʟᴜ", 
                    url=client.invitelink2
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ᴊᴏɪɴ ᴅᴜʟᴜ", 
                    url=client.invitelink4
                ),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if (
        FORCE_SUB_1
        and FORCE_SUB_3
        and FORCE_SUB_4
        and not FORCE_SUB_2
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="ᴊᴏɪɴ ᴅᴜʟᴜ", 
                    url=client.invitelink
                ),
                InlineKeyboardButton(
                    text="ᴊᴏɪɴ ᴅᴜʟᴜ", 
                    url=client.invitelink3
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ᴊᴏɪɴ ᴅᴜʟᴜ", 
                    url=client.invitelink4
                ),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if (
        FORCE_SUB_2
        and FORCE_SUB_3
        and FORCE_SUB_4
        and not FORCE_SUB_1
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="ᴊᴏɪɴ ᴅᴜʟᴜ", 
                    url=client.invitelink2
                ),
                InlineKeyboardButton(
                    text="ᴊᴏɪɴ ᴅᴜʟᴜ", 
                    url=client.invitelink3
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ᴊᴏɪɴ ᴅᴜʟᴜ", 
                    url=client.invitelink4
                ),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if (
        FORCE_SUB_1
        and FORCE_SUB_2
        and FORCE_SUB_3
        and FORCE_SUB_4
    ):
        buttons = [
            [
                InlineKeyboardButton(
                    text="ᴊᴏɪɴ ᴅᴜʟᴜ", 
                    url=client.invitelink
                ),
                InlineKeyboardButton(
                    text="ᴊᴏɪɴ ᴅᴜʟᴜ", 
                    url=client.invitelink2
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ᴊᴏɪɴ ᴅᴜʟᴜ", 
                    url=client.invitelink3
                ),
                InlineKeyboardButton(
                    text="ᴊᴏɪɴ ᴅᴜʟᴜ", 
                    url=client.invitelink4
                ),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
