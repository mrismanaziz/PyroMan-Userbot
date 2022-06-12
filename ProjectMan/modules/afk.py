# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import time

from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from ProjectMan import BOTLOG_CHATID
from ProjectMan.helpers.msg_types import Types, get_message_type
from ProjectMan.helpers.parser import escape_markdown
from ProjectMan.helpers.SQL.afk_db import get_afk, set_afk
from ProjectMan.modules.help import add_command_help

Owner = BOTLOG_CHATID
# Set priority to 11 and 12
MENTIONED = []
AFK_RESTIRECT = {}
DELAY_TIME = 3  # seconds


@Client.on_message(filters.me & filters.command("afk", cmd))
async def afk(client: Client, message: Message):
    karena = message.text.split(None, 1)[1] if len(message.command) != 1 else ""
    set_afk(True, karena)
    text = (
        "❏ {} **Telah AFK**!\n└ **Karena:** `{}`".format(client.me.mention, karena)
        if karena
        else "✘ {} **Telah AFK** ✘".format(client.me.mention)
    )
    await message.edit_text(text)


@Client.on_message(filters.mentioned & ~filters.bot, group=11)
async def afk_mentioned(client: Client, message: Message):
    global MENTIONED
    get = get_afk()
    if get and get["afk"]:
        if "-" in str(message.chat.id):
            cid = str(message.chat.id)[4:]
        else:
            cid = str(message.chat.id)

        if cid in list(AFK_RESTIRECT):
            if int(AFK_RESTIRECT[cid]) >= int(time.time()):
                return
        AFK_RESTIRECT[cid] = int(time.time()) + DELAY_TIME
        if get["reason"]:
            await message.reply(
                "❏ {} **Sedang AFK!**\n└ **Karena:** `{}`".format(
                    client.me.mention, get["reason"]
                )
            )
        else:
            await message.reply(f"**Maaf** {client.me.mention} **Sedang AFK!**")

        _, message_type = get_message_type(message)
        if message_type == Types.TEXT:
            if message.text:
                text = message.text
            else:
                text = message.caption
        else:
            text = message_type.name

        MENTIONED.append(
            {
                "user": message.from_user.first_name,
                "user_id": message.from_user.id,
                "chat": message.chat.title,
                "chat_id": cid,
                "text": text,
                "message_id": message.message_id,
            }
        )
        await client.send_message(
            Owner,
            "**#MENTION**\n • **Dari :** {}\n • **Grup :** `{}`\n • **Pesan :** `{}`".format(
                message.from_user.mention,
                message.chat.title,
                text[:3500],
            ),
        )


@Client.on_message(filters.me & filters.group, group=12)
async def no_longer_afk(client: Client, message: Message):
    global MENTIONED
    get = get_afk()
    if get and get["afk"]:
        await client.send_message(Owner, "Anda sudah tidak lagi AFK!")
        set_afk(False, "")
        text = "**Total {} Mention Saat Sedang AFK**\n".format(len(MENTIONED))
        for x in MENTIONED:
            msg_text = x["text"]
            if len(msg_text) >= 11:
                msg_text = "{}...".format(x["text"])
            text += "- [{}](https://t.me/c/{}/{}) ({}): {}\n".format(
                escape_markdown(x["user"]),
                x["chat_id"],
                x["message_id"],
                x["chat"],
                msg_text,
            )
        await client.send_message(Owner, text)
        MENTIONED = []


add_command_help(
    "afk",
    [
        [
            f"{cmd}afk <alasan>",
            "Memberi tahu orang yang menandai atau membalas salah satu pesan atau dm anda kalau anda sedang afk",
        ],
    ],
)
