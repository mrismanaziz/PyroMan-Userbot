# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER as cmd

from .help import *


@Client.on_message(filters.me & filters.command(["delspam", "deletespam"], cmd))
async def statspam(client: Client, message: Message):
    Man = await edit_or_reply(message, f"⚡ Usage: {cmd}delspam 10 Umm")
    quantity = message.command[1]
    spam_text = " ".join(message.command[2:])
    quantity = int(quantity)
    await message.delete()
    for i in range(quantity):
        await Man.delete()
        msg = await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.1)
        await msg.delete()
        await asyncio.sleep(0.1)


@Client.on_message(filters.me & filters.command(["spam", "spamming"], cmd))
async def sspam(client: Client, message: Message):
    Man = await edit_or_reply(message, f"⚡ Usage: {cmd}spam 10 Umm")
    quantity = message.command[1]
    spam_text = " ".join(message.command[2:])
    quantity = int(quantity)

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(
                message.chat.id, spam_text, reply_to_message_id=reply_to_id
            )
            await asyncio.sleep(0.15)
        return

    for _ in range(quantity):
        await Man.delete()
        await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.15)


@Client.on_message(filters.me & filters.command(["fastspam"], cmd))
async def fastspam(client: Client, message: Message):
    Man = await edit_or_reply(message, f"⚡ Usage: {cmd}fastspam 10 Umm")
    quantity = message.command[1]
    spam_text = " ".join(message.command[2:])
    quantity = int(quantity)

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(
                message.chat.id, spam_text, reply_to_message_id=reply_to_id
            )
            await asyncio.sleep(0.002)
        return

    for _ in range(quantity):
        await Man.delete()
        await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.002)


@Client.on_message(filters.me & filters.command(["slowspam", "delayspam"], cmd))
async def slowspam(client: Client, message: Message):
    Man = await edit_or_reply(message, f"⚡ Usage: {cmd}slowspam 10 Umm")
    quantity = message.command[1]
    spam_text = " ".join(message.command[2:])
    quantity = int(quantity)

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(
                message.chat.id, spam_text, reply_to_message_id=reply_to_id
            )
            await asyncio.sleep(0.9)
        return

    for _ in range(quantity):
        await Man.delete()
        await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.9)


@Client.on_message(
    filters.me & filters.command(["sspam", "stkspam", "spamstk", "stickerspam"], cmd)
)
async def spam_stick(client: Client, message: Message):
    if not message.reply_to_message:
        await edit_or_reply(
            message, "**reply to a sticker with amount you want to spam**"
        )
        return
    if not message.reply_to_message.sticker:
        await edit_or_reply(
            message, "**reply to a sticker with amount you want to spam**"
        )
        return
    else:
        i = 0
        times = message.command[1]
        if message.chat.type in ["supergroup", "group"]:
            for i in range(int(times)):
                sticker = message.reply_to_message.sticker.file_id
                await client.send_sticker(
                    message.chat.id,
                    sticker,
                )
                await asyncio.sleep(0.10)

        if umm.chat.type == "private":
            for i in range(int(times)):
                sticker = message.reply_to_message.sticker.file_id
                await client.send_sticker(message.chat.id, sticker)
                await asyncio.sleep(0.10)


add_command_help(
    "spam",
    [
        [f"{cmd}delspam", "It will Spam then delete it's spam automatically."],
        [f"{cmd}spam", "Spam Your Custom Message  (Sudo User also)."],
        [f"{cmd}sspam", "Sticker Spam  (Sudo Users also)."],
        [f"{cmd}delayspam", "Spam Slowly (Sudo User also)."],
        [f"{cmd}fastspam", "Spam Your message fastly  (Sudo User also)."],
    ],
)
