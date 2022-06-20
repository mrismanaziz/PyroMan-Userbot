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

from config import CMD_HANDLER as cmd
from config import *
from ProjectMan import *
from ProjectMan.helpers.basic import edit_or_reply
from ProjectMan.utils import get_readable_time

from .help import add_command_help

modules = CMD_HELP
emoji = ALIVE_EMOJI
alive_text = ALIVE_TEKS_CUSTOM


@Client.on_message(filters.command(["alive", "awake"], cmd) & filters.me)
async def alive(client: Client, message: Message):
    xx = await edit_or_reply(message, "⚡️")
    apa = client.send_video if ALIVE_LOGO.endswith(".mp4") else client.send_photo
    uptime = await get_readable_time((time.time() - StartTime))
    capt = (
        f"**[PyroMan-Userbot](https://github.com/mrismanaziz/PyroMan-Userbot) is Up and Running.**\n\n"
        f"**{alive_text}**\n\n"
        f"{emoji} **Master :** {client.me.mention} \n"
        f"{emoji} **Modules :** `{len(modules)} Modules` \n"
        f"{emoji} **Bot Version :** `{BOT_VER}` \n"
        f"{emoji} **Python Version :** `{python_version()}` \n"
        f"{emoji} **Pyrogram Version :** `{versipyro}` \n"
        f"{emoji} **Bot Uptime :** `{uptime}` \n\n"
        f"    **[𝗦𝘂𝗽𝗽𝗼𝗿𝘁](https://t.me/{GROUP})** | **[𝗖𝗵𝗮𝗻𝗻𝗲𝗹](https://t.me/{CHANNEL})** | **[𝗢𝘄𝗻𝗲𝗿](tg://user?id={client.me.id})**"
    )
    await asyncio.gather(xx.delete(), apa(message.chat.id, ALIVE_LOGO, caption=capt))


add_command_help(
    "alive",
    [
        [
            f"{cmd}alive",
            "Perintah ini untuk memeriksa userbot anda berfungsi atau tidak",
        ]
    ],
)
