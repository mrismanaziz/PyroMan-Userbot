# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio
import time
from platform import python_version

from pyrogram import Client
from pyrogram import __version__ as versipyro
from pyrogram import filters
from pyrogram.types import Message

from config import ALIVE_EMOJI, ALIVE_LOGO, ALIVE_TEKS_CUSTOM, BOT_VER, CHANNEL
from config import CMD_HANDLER as cmd
from config import GROUP
from ProjectMan import CMD_HELP, StartTime
from ProjectMan.helpers.basic import edit_or_reply
from ProjectMan.helpers.PyroHelpers import ReplyCheck
from ProjectMan.utils import get_readable_time

from .help import add_command_help

modules = CMD_HELP
emoji = ALIVE_EMOJI
alive_text = ALIVE_TEKS_CUSTOM


@Client.on_message(filters.command(["alive", "awake"], cmd) & filters.me)
async def alive(client: Client, message: Message):
    xx = await edit_or_reply(message, "⚡️")
    await asyncio.sleep(2)
    apa = client.send_video if ALIVE_LOGO.endswith(".mp4") else client.send_photo
    uptime = await get_readable_time((time.time() - StartTime))
    capt = (
        f"**[PyroMan-Userbot](https://github.com/mrismanaziz/PyroMan-Userbot) is Up and Running.**\n\n"
        f"<b>{alive_text}</b>\n\n"
        f"{emoji} <b>Master :</b> {client.me.mention} \n"
        f"{emoji} <b>Modules :</b> <code>{len(modules)} Modules</code> \n"
        f"{emoji} <b>Bot Version :</b> <code>{BOT_VER}</code> \n"
        f"{emoji} <b>Python Version :</b> <code>{python_version()}</code> \n"
        f"{emoji} <b>Pyrogram Version :</b> <code>{versipyro}</code> \n"
        f"{emoji} <b>Bot Uptime :</b> <code>{uptime}</code> \n\n"
        f"    **[𝗦𝘂𝗽𝗽𝗼𝗿𝘁](https://t.me/{GROUP})** | **[𝗖𝗵𝗮𝗻𝗻𝗲𝗹](https://t.me/{CHANNEL})** | **[𝗢𝘄𝗻𝗲𝗿](tg://user?id={client.me.id})**"
    )
    await asyncio.gather(
        xx.delete(),
        apa(
            message.chat.id,
            ALIVE_LOGO,
            caption=capt,
            reply_to_message_id=ReplyCheck(message),
        ),
    )


add_command_help(
    "alive",
    [
        [
            "alive",
            "Perintah ini untuk memeriksa userbot anda berfungsi atau tidak",
        ]
    ],
)
