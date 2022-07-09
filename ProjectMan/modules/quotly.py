# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio
import random
from asyncio import sleep

from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from ProjectMan import *
from ProjectMan.helpers.basic import edit_or_reply

from .help import *


@Client.on_message(filters.me & filters.command(["q", "quotly"], cmd))
async def quotly(bot: Client, message: Message):
    if not message.reply_to_message:
        return await edit_or_reply(message, "Reply to any users text message")
    Man = await edit_or_reply(message, "```Making a Quote```")
    await message.reply_to_message.forward("@QuotLyBot")
    is_sticker = False
    progress = 0
    while not is_sticker:
        try:
            await sleep(4)
            msg = await bot.get_history("@QuotLyBot", 1)
            is_sticker = True
        except:
            await sleep(1)
            progress += random.randint(0, 5)
            if progress > 100:
                await Man.edit("There was a long running error")
                return
            try:
                await Man.edit("```Making a Quote\nProcessing {}%```".format(progress))
            except:
                await Man.edit("ERROR")

    if msg_id := msg[0]["message_id"]:
        await asyncio.gather(
            Man.delete(),
            bot.copy_message(message.chat.id, "@QuotLyBot", msg_id),
        )


add_command_help(
    "quotly",
    [
        [
            f"q atau {cmd}quotly",
            "To Make a Quote",
        ],
    ],
)
