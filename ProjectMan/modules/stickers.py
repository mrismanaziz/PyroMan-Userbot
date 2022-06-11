# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio
import os
from io import BytesIO

from pyrogram import Client, filters
from pyrogram.errors import StickersetInvalid, YouBlockedUser
from pyrogram.raw.functions.messages import GetStickerSet
from pyrogram.raw.types import InputStickerSetShortName
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from ProjectMan.helpers.PyroHelpers import ReplyCheck
from ProjectMan.helpers.tools import convert_to_image, get_text, resize_image

from .help import add_command_help


@Client.on_message(filters.command(["packinfo", "stickerinfo"], cmd) & filters.me)
async def packinfo(client: Client, message: Message):
    rep = await message.edit_text("`Processing...`")
    if not message.reply_to_message:
        await rep.edit("Please Reply To Sticker...")
        return
    if not message.reply_to_message.sticker:
        await rep.edit("Please Reply To A Sticker...")
        return
    if not message.reply_to_message.sticker.set_name:
        await rep.edit("`Seems Like A Stray Sticker!`")
        return
    stickerset = await client.send(
        GetStickerSet(
            stickerset=InputStickerSetShortName(
                short_name=message.reply_to_message.sticker.set_name
            ),
            hash=0,
        )
    )
    emojis = []
    for stucker in stickerset.packs:
        if stucker.emoticon not in emojis:
            emojis.append(stucker.emoticon)
    output = f"""**Sticker Pack Title **: `{stickerset.set.title}`
**Sticker Pack Short Name **: `{stickerset.set.short_name}`
**Stickers Count **: `{stickerset.set.count}`
**Archived **: `{stickerset.set.archived}`
**Official **: `{stickerset.set.official}`
**Masks **: `{stickerset.set.masks}`
**Animated **: `{stickerset.set.animated}`
**Emojis In Pack **: `{' '.join(emojis)}`
"""
    await rep.edit(output)


@Client.on_message(filters.command(["tikel", "kang"], cmd) & filters.me)
async def kang(client: Client, message: Message):
    rep = await message.edit_text("`Boleh juga ni stickernya colong ahh...`")
    if not message.reply_to_message:
        await rep.edit("Please Reply To Sticker...")
        return
    Hell = get_text(message)
    pack = 1
    f_name = message.from_user.first_name
    packname = f"Sticker Pack {f_name} Vol.{pack}"
    packshortname = f"Sticker_u{message.from_user.id}_{pack}"
    emoji = "✨"
    try:
        Hell = Hell.strip()
        if not Hell.isalpha():
            if not Hell.isnumeric():
                emoji = Hell
        else:
            emoji = "✨"
    except:
        emoji = "✨"
    exist = None
    is_anim = False
    if message.reply_to_message.sticker:
        if not Hell:
            emoji = message.reply_to_message.sticker.emoji or "✨"
        is_anim = message.reply_to_message.sticker.is_animated
        if is_anim:
            packshortname += "_animated"
            packname += " Animated"
        if message.reply_to_message.sticker.mime_type == "application/x-tgsticker":
            file_name = await message.reply_to_message.download("AnimatedSticker.tgs")
        else:
            cool = await convert_to_image(message, client)
            if not cool:
                await rep.edit("`Reply to a valid media first.`")
                return
            file_name = resize_image(cool)
    elif message.reply_to_message.document:
        if message.reply_to_message.document.mime_type == "application/x-tgsticker":
            is_anim = True
            packshortname += "_animated"
            packname += " Animated"
            file_name = await message.reply_to_message.download("AnimatedSticker.tgs")
    else:
        cool = await convert_to_image(message, client)
        if not cool:
            await rep.edit("`Reply to a valid media first.`")
            return
        file_name = resize_image(cool)
    try:
        exist = await client.send(
            GetStickerSet(
                stickerset=InputStickerSetShortName(short_name=packshortname),
                hash=0,
            )
        )
    except StickersetInvalid:
        pass
    if exist:
        try:
            await client.send_message("stickers", "/addsticker")
        except YouBlockedUser:
            await client.unblock_user("stickers")
            await client.send_message("stickers", "/addsticker")
        await asyncio.sleep(2)
        await client.send_message("stickers", packshortname)
        await asyncio.sleep(2)
        limit = "50" if is_anim else "120"
        messi = (await client.get_history("stickers", 1))[0]
        while limit in messi.text:
            pack += 1
            prev_pack = int(pack) - 1
            await rep.edit(
                f"Kang Pack Vol __{prev_pack}__ is Full! Switching To Vol __{pack}__ Kang Pack"
            )
            f_name = message.from_user.first_name
            packname = f"Sticker Pack {f_name} Vol.{pack}"
            packshortname = f"Sticker_u{message.from_user.id}_{pack}"
            if is_anim:
                packshortname += "_animated"
                packname += " Animated"
            await client.send_message("stickers", packshortname)
            await asyncio.sleep(2)
            messi = (await client.get_history("stickers", 1))[0]
            if messi.text == "Invalid pack selected.":
                if is_anim:
                    await client.send_message("stickers", "/newanimated")
                else:
                    await client.send_message("stickers", "/newpack")
                await asyncio.sleep(2)
                await client.send_message("stickers", packname)
                await asyncio.sleep(2)
                await client.send_document("stickers", file_name)
                await asyncio.sleep(2)
                await client.send_message("stickers", emoji)
                await asyncio.sleep(2)
                await client.send_message("stickers", "/publish")
                if is_anim:
                    await client.send_message("stickers", packname)
                await asyncio.sleep(2)
                await client.send_message("stickers", "/skip")
                await asyncio.sleep(2)
                await client.send_message("stickers", packshortname)
                await rep.edit(
                    f"**Sticker Berhasil Ditambahkan!**\n         🔥 **[KLIK DISINI](https://t.me/addstickers/{packshortname})** 🔥\n**Untuk Menggunakan Stickers**"
                )
                return
        await client.send_document("stickers", file_name)
        await asyncio.sleep(2)
        await client.send_message("stickers", emoji)
        await asyncio.sleep(2)
        await client.send_message("stickers", "/done")
        await rep.edit(
            f"**Sticker Berhasil Ditambahkan!**\n         🔥 **[KLIK DISINI](https://t.me/addstickers/{packshortname})** 🔥\n**Untuk Menggunakan Stickers**"
        )
    else:
        if is_anim:
            await client.send_message("stickers", "/newanimated")
        else:
            await client.send_message("stickers", "/newpack")
        await asyncio.sleep(2)
        await client.send_message("stickers", packname)
        await asyncio.sleep(2)
        await client.send_document("stickers", file_name)
        await asyncio.sleep(2)
        await client.send_message("stickers", emoji)
        await asyncio.sleep(2)
        await client.send_message("stickers", "/publish")
        await asyncio.sleep(2)
        if is_anim:
            await client.send_message("stickers", packname)
        await asyncio.sleep(2)
        await client.send_message("stickers", "/skip")
        await asyncio.sleep(2)
        await client.send_message("stickers", packshortname)
        await rep.edit(
            f"**Sticker Berhasil Ditambahkan!**\n         🔥 **[KLIK DISINI](https://t.me/addstickers/{packshortname})** 🔥\n**Untuk Menggunakan Stickers**"
        )
        if os.path.exists(file_name):
            os.remove(file_name)


@Client.on_message(filters.command(["get", "getsticker"], cmd) & filters.me)
async def stick2png(client: Client, message: Message):
    try:
        await message.edit("<b>Downloading...</b>")

        path = await message.reply_to_message.download()
        with open(path, "rb") as f:
            content = f.read()
        os.remove(path)

        file_io = BytesIO(content)
        file_io.name = "sticker.png"

        await client.send_photo(
            message.chat.id, file_io, reply_to_message_id=ReplyCheck(message)
        )
    except Exception as e:
        await message.edit(f"{e}")
    else:
        await message.delete()


add_command_help(
    "sticker",
    [
        [
            f"{cmd}kang atau {cmd}tikel",
            f"Balas {cmd}kang Ke Sticker Atau Gambar Untuk Menambahkan Ke Sticker Pack.",
        ],
        [
            f"{cmd}kang [emoji] atau {cmd}tikel [emoji]",
            f"Untuk Menambahkan dan costum emoji sticker Ke Sticker Pack Mu.\n\n`  •  **NOTE:** Untuk Membuat Sticker Pack baru Gunakan angka dibelakang {cmd}kang\n  •  **CONTOH:** {cmd}kang 2 untuk membuat dan menyimpan ke sticker pack ke 2`",
        ],
        [
            f"{cmd}packinfo atau {cmd}stickerinfo",
            "Untuk Mendapatkan Informasi Sticker Pack.",
        ],
        [f"{cmd}get", "Balas ke sticker untuk mendapatkan foto sticker."],
    ],
)
