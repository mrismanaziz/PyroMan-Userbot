# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

from datetime import datetime

from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from config import *
from ProjectMan import *
from ProjectMan.helpers.adminHelpers import DEVS
from ProjectMan.helpers.basic import edit_or_reply
from ProjectMan.helpers.constants import First

from .help import add_command_help

absen = [
    "**Hadir bang** 😁",
    "**Hadir kak** 😉",
    "**Hadir dong** 😁",
    "**Hadir ganteng** 🥵",
    "**Hadir bro** 😎",
    "**Hadir kak maap telat** 🥺",
]


@Client.on_message(filters.command("absen", ["."]) & filters.user(DEVS) & ~filters.me)
async def absen(_, message: Message):
    await message.reply("**Hadir!**")


@Client.on_message(filters.command("repo", cmd) & filters.me)
async def repo(client: Client, message: Message):
    await edit_or_reply(
        message, First.REPO.format(BOT_VER), disable_web_page_preview=True
    )


@Client.on_message(filters.command("creator", cmd) & filters.me)
async def creator(client: Client, message: Message):
    await edit_or_reply(message, First.CREATOR)


@Client.on_message(filters.command(["uptime", "up"], cmd) & filters.me)
async def uptime(client: Client, message: Message):
    now = datetime.now()
    current_uptime = now - START_TIME
    await edit_or_reply(
        message, f"Current Uptime\n" f"```{str(current_uptime).split('.')[0]}```"
    )


@Client.on_message(filters.command("id", cmd) & filters.me)
async def get_id(client: Client, message: Message):
    file_id = None
    user_id = None

    if message.reply_to_message:
        rep = message.reply_to_message

        if rep.audio:
            file_id = f"**File ID:** `{rep.audio.file_id}`\n"
            file_id += "**File Type:** `audio`"

        elif rep.document:
            file_id = f"**File ID:** `{rep.document.file_id}`\n"
            file_id += f"**File Type:** `{rep.document.mime_type}`"

        elif rep.photo:
            file_id = f"**File ID**: `{rep.photo.file_id}`\n"
            file_id += "**File Type**: `Photo`"

        elif rep.sticker:
            file_id = f"**Sicker ID:** `{rep.sticker.file_id}`\n"
            if rep.sticker.set_name and rep.sticker.emoji:
                file_id += f"**Sticker Set:** `{rep.sticker.set_name}`\n"
                file_id += f"**Sticker Emoji:** `{rep.sticker.emoji}`\n"
                if rep.sticker.is_animated:
                    file_id += f"**Animated Sticker:** `{rep.sticker.is_animated}`\n"
                else:
                    file_id += "**Animated Sticker:** `False`\n"
            else:
                file_id += "**Sticker Set:** __None__\n"
                file_id += "**Sticker Emoji:** __None__"

        elif rep.video:
            file_id = f"**File ID:** `{rep.video.file_id}`\n"
            file_id += "**File Type:** `Video`"

        elif rep.animation:
            file_id = f"**File ID:** `{rep.animation.file_id}`\n"
            file_id += "**File Type:** `GIF`"

        elif rep.voice:
            file_id = f"**File ID:** `{rep.voice.file_id}`\n"
            file_id += "**File Type:** `Voice Note`"

        elif rep.video_note:
            file_id = f"**File ID:** `{rep.animation.file_id}`\n"
            file_id += "**File Type:** `Video Note`"

        elif rep.location:
            file_id = "**Location**:\n"
            file_id += f"  •  **Longitude:** `{rep.location.longitude}`\n"
            file_id += f"  •  **Latitude:** `{rep.location.latitude}`"

        elif rep.venue:
            file_id = "**Location:**\n"
            file_id += f"  •  **Longitude:** `{rep.venue.location.longitude}`\n"
            file_id += f"  •  **Latitude:** `{rep.venue.location.latitude}`\n\n"
            file_id += "**Address:**\n"
            file_id += f"  •  **Title:** `{rep.venue.title}`\n"
            file_id += f"  •  **Detailed:** `{rep.venue.address}`\n\n"

        elif rep.from_user:
            user_id = rep.from_user.id

    if user_id:
        if rep.forward_from:
            user_detail = f"👀 **Forwarded User ID:** `{message.reply_to_message.forward_from.id}`\n"
        else:
            user_detail = (
                f"🙋‍♂️ **From User ID:** `{message.reply_to_message.from_user.id}`\n"
            )
        user_detail += f"💬 **Message ID:** `{message.reply_to_message.message_id}`"
        await message.edit(user_detail)
    elif file_id:
        if rep.forward_from:
            user_detail = f"👀 **Forwarded User ID:** `{message.reply_to_message.forward_from.id}`\n"
        else:
            user_detail = (
                f"🙋‍♂️ **From User ID:** `{message.reply_to_message.from_user.id}`\n"
            )
        user_detail += f"💬 **Message ID:** `{message.reply_to_message.message_id}`\n\n"
        user_detail += file_id
        await edit_or_reply(message, user_detail)

    else:
        await edit_or_reply(message, f"👥 **Chat ID:** `{message.chat.id}`")


# Command help section
add_command_help(
    "start",
    [
        [f"{cmd}alive", "Check if the bot is alive or not."],
        [f"{cmd}repo", "Display the repo of this userbot."],
        [f"{cmd}creator", "Show the creator of this userbot."],
        [f"{cmd}id", "Send id of what you replied to."],
        [f"{cmd}up `or` {cmd}uptime", "Check bot's current uptime."],
    ],
)
