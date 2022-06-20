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

from config import BLACKLIST_CHAT
from config import CMD_HANDLER as cmd
from ProjectMan.helpers.adminHelpers import BLACKLIST_CHAT, DEVS
from ProjectMan.helpers.basic import edit_or_reply
from ProjectMan.helpers.PyroHelpers import ReplyCheck
from ProjectMan.utils import extract_user

from .help import add_command_help


@Client.on_message(filters.command("jamet", cmd) & filters.me)
async def ngejamet(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    xx = await edit_or_reply(message, "**WOII**")
    await asyncio.sleep(1.5)
    await xx.edit("**JAMET**")
    await asyncio.sleep(1.5)
    await xx.edit("**CUMA MAU BILANG**")
    await asyncio.sleep(1.5)
    await xx.edit("**GAUSAH SO ASIK**")
    await asyncio.sleep(1.5)
    await xx.edit("**EMANG KENAL?**")
    await asyncio.sleep(1.5)
    await xx.edit("**GAUSAH REPLY**")
    await asyncio.sleep(1.5)
    await xx.edit("**KITA BUKAN KAWAN**")
    await asyncio.sleep(1.5)
    await xx.edit("**GASUKA PC ANJING**")
    await asyncio.sleep(1.5)
    await xx.edit("**BOCAH KAMPUNG**")
    await asyncio.sleep(1.5)
    await xx.edit("**MENTAL TEMPE**")
    await asyncio.sleep(1.5)
    await xx.edit("**LEMBEK NGENTOT🔥**")


@Client.on_message(filters.command("ywc", cmd) & filters.me)
async def ywc(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "ok sama sama",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("pp", cmd) & filters.me)
async def toxicpp(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "PASANG PP DULU GOBLOK,BIAR ORANG-ORANG PADA TAU BETAPA HINA NYA MUKA LU 😆",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("dp", cmd) & filters.me)
async def toxicdp(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "MUKA LU HINA, GAUSAH SOK KERAS YA ANJENGG!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("so", cmd) & filters.me)
async def toxicso(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "GAUSAH SOKAB SAMA GUA GOBLOK, LU BABU GA LEVEL!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("nb", cmd) & filters.me)
async def toxicnb(client: Client, message: Message):
    user_id = await extract_user(message)
    if message.chat.id in BLACKLIST_CHAT:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan di Group ini**"
        )
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "MAEN BOT MULU ALAY NGENTOTT, KESANNYA NORAK GOBLOK!!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("met", cmd) & filters.me)
async def toxicmet(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "NAMANYA JUGA JAMET CAPER SANA SINI BUAT CARI NAMA",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("war", cmd) & filters.me)
async def toxicwer(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "WAR WAR PALAK BAPAK KAU WAR, SOK KERAS BANGET GOBLOK, DI TONGKRONGAN JADI BABU, DI TELE SOK JAGOAN.",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("wartai", cmd) & filters.me)
async def toxicwartai(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "WAR WAR TAI ANJING, KETRIGGER MINTA SHARELOK LU KIRA MAU COD-AN GOBLOK, BACOTAN LU AJA KGA ADA KERAS KERASNYA GOBLOK",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("kismin", cmd) & filters.me)
async def toxickismin(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "CUIHHHH, MAKAN AJA MASIH NGEMIS LO GOBLOK, JANGAN SO NINGGI YA KONTOL GA KEREN LU KEK GITU GOBLOK!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("ded", cmd) & filters.me)
async def toxicded(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "MATI AJA LU GOBLOK, GAGUNA LU HIDUP DI BUMI",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("sokab", cmd) & filters.me)
async def toxicsokab(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "SOKAB BET LU GOBLOK, KAGA ADA ISTILAH NYA BAWAHAN TEMENAN AMA BOS!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("gembel", cmd) & filters.me)
async def toxicgembel(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "MUKA BAPAK LU KEK KELAPA SAWIT ANJING, GA USAH NGATAIN ORANG, MUKA LU AJA KEK GEMBEL TEXAS GOBLOK!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("cuih", cmd) & filters.me)
async def toxiccuih(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "GAK KEREN LO KEK BEGITU GOBLOK, KELUARGA LU BAWA SINI GUA LUDAHIN SATU-SATU. CUIHH!!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("dih", cmd) & filters.me)
async def toxicdih(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "DIHHH NAJISS ANAK HARAM LO GOBLOK, JANGAN BELAGU DIMARI KAGA KEREN LU KEK BGITU TOLOL!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("gcs", cmd) & filters.me)
async def toxicgcs(client: Client, message: Message):
    user_id = await extract_user(message)
    if message.chat.id in BLACKLIST_CHAT:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan di Group ini**"
        )
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "GC SAMPAH KAYA GINI, BUBARIN AJA GOBLOK!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("skb", cmd) & filters.me)
async def toxicskb(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "EMANG KITA KENAL? KAGA GOBLOK SOKAB BANGET LU GOBLOK",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("virtual", cmd) & filters.me)
async def toxicvirtual(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    xx = await edit_or_reply(message, "**OOOO**")
    await asyncio.sleep(1.5)
    await xx.edit("**INI YANG VIRTUAL**")
    await asyncio.sleep(1.5)
    await xx.edit("**YANG KATANYA SAYANG BANGET**")
    await asyncio.sleep(1.5)
    await xx.edit("**TAPI TETEP AJA DI TINGGAL**")
    await asyncio.sleep(1.5)
    await xx.edit("**NI INGET**")
    await asyncio.sleep(1.5)
    await xx.edit("**TANGANNYA AJA GA BISA DI PEGANG**")
    await asyncio.sleep(1.5)
    await xx.edit("**APALAGI OMONGANNYA**")
    await asyncio.sleep(1.5)
    await xx.edit("**BHAHAHAHA**")
    await asyncio.sleep(1.5)
    await xx.edit("**KASIAN MANA MASIH MUDA**")


add_command_help(
    "toxic",
    [
        [f"{cmd}jamet", "Menghina Jamet telegram"],
        [f"{cmd}pp", "Menghina Jamet telegram yang ga pake foto profil."],
        [f"{cmd}dp", "Menghina Jamet muka hina!"],
        [f"{cmd}so", "Ngeledek orang sokab."],
        [f"{cmd}nb", "Ngeledek orang norak baru pake bot."],
        [f"{cmd}skb", "Ngeledek orang sokab versi 2."],
        [f"{cmd}met", "Ngeledek si jamet caper."],
        [f"{cmd}war", "Ngeledek orang so keras ngajak war."],
        [f"{cmd}wartai", "Ngeledek orang so ketrigger ngajak cod minta sharelok."],
        [f"{cmd}kismin", "Ngeledek orang kismin so jagoan di tele."],
        [f"{cmd}ded", "Nyuruh orang mati aja goblok wkwk."],
        [f"{cmd}sokab", "Ngeledek orang so kenal so dekat padahal kga kenal goblok."],
        [f"{cmd}gembel", "Ngeledek bapaknya si jamet."],
        [f"{cmd}cuih", "Ngeludahin keluarganya satu satu wkwk."],
        [f"{cmd}dih", "Ngeledek anak haram."],
        [f"{cmd}gcs", "Ngeledek gc sampah."],
    ],
)
