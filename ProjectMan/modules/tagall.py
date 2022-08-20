# Copyright (C) 2020-2021 by Toni880@Github, < https://github.com/Toni880 >.
#
# This file is part of < https://github.com/Toni880/Prime-Userbot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Toni880/Prime-Userbot/blob/master/LICENSE >
#
# All rights reserved. Ken-Kan

from asyncio import sleep

from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from ProjectMan.helpers.tools import get_arg

from .help import add_command_help

spam_chats = []


@Client.on_message(filters.command("tagall", cmd) & filters.me)
async def mentionall(client: Client, message: Message):
    await message.delete()
    chat_id = message.chat.id
    direp = message.reply_to_message
    args = get_arg(message)
    if not direp and not args:
        return await message.edit("**Berikan saya pesan atau balas ke pesan!**")

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}), "
        if usrnum == 5:
            if args:
                txt = f"{args}\n{usrtxt}"
                await client.send_message(chat_id, txt)
            elif direp:
                await direp.reply(usrtxt)
            await sleep(2)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@Client.on_message(filters.command("cancel", cmd) & filters.me)
async def cancel_spam(client: Client, message: Message):
    if not message.chat.id in spam_chats:
        return await message.edit("**Sepertinya tidak ada tagall disini.**")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.edit("**Memberhentikan Mention.**")


add_command_help(
    "tagall",
    [
        [
            "tagall [text/reply ke chat]",
            "Untuk Mention semua member group",
        ],
        [
            "cancel",
            f"Untuk Membatalkan Perintah {cmd}tagall",
        ],
    ],
)
