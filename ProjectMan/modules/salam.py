# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

from asyncio import sleep

from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from ProjectMan.helpers.basic import edit_or_reply
from ProjectMan.helpers.PyroHelpers import ReplyCheck

from .help import add_command_help


@Client.on_message(filters.command("p", cmd) & filters.me)
async def salamone(client: Client, message: Message):
    await client.send_message(
        message.chat.id,
        "Assalamualaikum",
        reply_to_message_id=ReplyCheck(message),
    )
    await message.delete()


@Client.on_message(filters.command("pe", cmd) & filters.me)
async def salamdua(client: Client, message: Message):
    await client.send_message(
        message.chat.id,
        "Assalamualaikum Warahmatullahi Wabarakatuh",
        reply_to_message_id=ReplyCheck(message),
    )
    await message.delete()


@Client.on_message(filters.command("l", cmd) & filters.me)
async def jwbsalam(client: Client, message: Message):
    await client.send_message(
        message.chat.id, "Wa'alaikumsalam", reply_to_message_id=ReplyCheck(message)
    )
    await message.delete()


@Client.on_message(filters.command("el", cmd) & filters.me)
async def jwbsalamlngkp(client: Client, message: Message):
    await client.send_message(
        message.chat.id,
        "Wa'alaikumsalam Warahmatullahi Wabarakatuh",
        reply_to_message_id=ReplyCheck(message),
    )
    await message.delete()


@Client.on_message(filters.command("a", cmd) & filters.me)
async def salken(client: Client, message: Message):
    xx = await edit_or_reply(message, f"**Haii Salken Saya {client.me.first_name}**")
    sleep(2)
    await xx.edit("Assalamualaikum")


@Client.on_message(filters.command("ass", cmd) & filters.me)
async def salamarab(client: Client, message: Message):
    xx = await edit_or_reply(message, "Salam Dulu Biar Sopan")
    sleep(2)
    await xx.edit("السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")


@Client.on_message(filters.command("j", cmd) & filters.me)
async def jakasem(client: Client, message: Message):
    xx = await edit_or_reply(message, "**JAKA SEMBUNG BAWA GOLOK**")
    sleep(3)
    await xx.edit("**NIMBRUNG GOBLOKK!!!🔥**")


@Client.on_message(filters.command("k", cmd) & filters.me)
async def ngegas(client: Client, message: Message):
    xx = await edit_or_reply(message, f"**Hallo KIMAAKK SAYA {client.me.first_name}**")
    sleep(2)
    await xx.edit("**LU SEMUA NGENTOT 🔥**")


add_command_help(
    "salam",
    [
        [f"{cmd}p", "Assalamualaikum."],
        [f"{cmd}pe", "Assalamualaikum Warahmatullahi Wabarakatuh."],
        [f"{cmd}l`", "Wa'alaikumsalam."],
        [f"{cmd}ass`", "Assalamualaikum Bahas arab."],
        [f"{cmd}a`", "Salam Kenal dan salam."],
        [f"{cmd}l`", "Wa'alaikumsalam."],
        [f"{cmd}el`", "Wa'alaikumsalam Warahmatullahi Wabarakatuh."],
    ],
)
