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

import cv2
import requests
from bs4 import BeautifulSoup as bs
from PIL import Image
from pyrogram import Client, emoji, filters
from pyrogram.enums import ParseMode
from pyrogram.errors import StickersetInvalid, YouBlockedUser
from pyrogram.raw.functions.messages import GetStickerSet
from pyrogram.raw.types import InputStickerSetShortName
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from ProjectMan.helpers.basic import edit_or_reply
from ProjectMan.helpers.PyroHelpers import ReplyCheck
from ProjectMan.helpers.tools import get_arg, get_text, resize_media
from ProjectMan.utils.tools import add_text_img, bash

from .help import add_command_help


@Client.on_message(filters.command(["tikel", "kang"], cmd) & filters.me)
async def kang(client: Client, message: Message):
    user = client.me
    replied = message.reply_to_message
    Man = await edit_or_reply(message, "`Boleh juga ni stickernya colong ahh...`")
    media_ = None
    emoji_ = None
    is_anim = False
    is_video = False
    resize = False
    ff_vid = False
    if replied and replied.media:
        if replied.photo:
            resize = True
        elif replied.document and "image" in replied.document.mime_type:
            resize = True
            replied.document.file_name
        elif replied.document and "tgsticker" in replied.document.mime_type:
            is_anim = True
            replied.document.file_name
        elif replied.document and "video" in replied.document.mime_type:
            resize = True
            is_video = True
            ff_vid = True
        elif replied.animation:
            resize = True
            is_video = True
            ff_vid = True
        elif replied.video:
            resize = True
            is_video = True
            ff_vid = True
        elif replied.sticker:
            if not replied.sticker.file_name:
                await Man.edit("**Stiker tidak memiliki Nama!**")
                return
            emoji_ = replied.sticker.emoji
            is_anim = replied.sticker.is_animated
            is_video = replied.sticker.is_video
            if not (
                replied.sticker.file_name.endswith(".tgs")
                or replied.sticker.file_name.endswith(".webm")
            ):
                resize = True
                ff_vid = True
        else:
            await Man.edit("**File Tidak Didukung**")
            return
        media_ = await client.download_media(replied, file_name="ProjectMan/resources/")
    else:
        await Man.edit("**Silahkan Reply ke Media Foto/GIF/Sticker!**")
        return
    if media_:
        args = get_text(message)
        pack = 1
        if len(args) == 2:
            emoji_, pack = args
        elif len(args) == 1:
            if args[0].isnumeric():
                pack = int(args[0])
            else:
                emoji_ = args[0]

        if emoji_ and emoji_ not in (
            getattr(emoji, _) for _ in dir(emoji) if not _.startswith("_")
        ):
            emoji_ = None
        if not emoji_:
            emoji_ = "✨"

        u_name = user.username
        u_name = "@" + u_name if u_name else user.first_name or user.id
        packname = f"Sticker_u{user.id}_v{pack}"
        custom_packnick = f"{u_name} Sticker Pack"
        packnick = f"{custom_packnick} Vol.{pack}"
        cmd = "/newpack"
        if resize:
            media_ = await resize_media(media_, is_video, ff_vid)
        if is_anim:
            packname += "_animated"
            packnick += " (Animated)"
            cmd = "/newanimated"
        if is_video:
            packname += "_video"
            packnick += " (Video)"
            cmd = "/newvideo"
        exist = False
        while True:
            try:
                exist = await client.invoke(
                    GetStickerSet(
                        stickerset=InputStickerSetShortName(short_name=packname), hash=0
                    )
                )
            except StickersetInvalid:
                exist = False
                break
            limit = 50 if (is_video or is_anim) else 120
            if exist.set.count >= limit:
                pack += 1
                packname = f"a{user.id}_by_userge_{pack}"
                packnick = f"{custom_packnick} Vol.{pack}"
                if is_anim:
                    packname += f"_anim{pack}"
                    packnick += f" (Animated){pack}"
                if is_video:
                    packname += f"_video{pack}"
                    packnick += f" (Video){pack}"
                await Man.edit(
                    f"`Membuat Sticker Pack Baru {pack} Karena Sticker Pack Sudah Penuh`"
                )
                continue
            break
        if exist is not False:
            try:
                await client.send_message("stickers", "/addsticker")
            except YouBlockedUser:
                await client.unblock_user("stickers")
                await client.send_message("stickers", "/addsticker")
            except Exception as e:
                return await Man.edit(f"**ERROR:** `{e}`")
            await asyncio.sleep(2)
            await client.send_message("stickers", packname)
            await asyncio.sleep(2)
            limit = "50" if is_anim else "120"
            while limit in await get_response(message, client):
                pack += 1
                packname = f"a{user.id}_by_{user.username}_{pack}"
                packnick = f"{custom_packnick} vol.{pack}"
                if is_anim:
                    packname += "_anim"
                    packnick += " (Animated)"
                if is_video:
                    packname += "_video"
                    packnick += " (Video)"
                await Man.edit(
                    "`Membuat Sticker Pack Baru "
                    + str(pack)
                    + " Karena Sticker Pack Sudah Penuh`"
                )
                await client.send_message("stickers", packname)
                await asyncio.sleep(2)
                if await get_response(message, client) == "Invalid pack selected.":
                    await client.send_message("stickers", cmd)
                    await asyncio.sleep(2)
                    await client.send_message("stickers", packnick)
                    await asyncio.sleep(2)
                    await client.send_document("stickers", media_)
                    await asyncio.sleep(2)
                    await client.send_message("Stickers", emoji_)
                    await asyncio.sleep(2)
                    await client.send_message("Stickers", "/publish")
                    await asyncio.sleep(2)
                    if is_anim:
                        await client.send_message(
                            "Stickers", f"<{packnick}>", parse_mode=ParseMode.MARKDOWN
                        )
                        await asyncio.sleep(2)
                    await client.send_message("Stickers", "/skip")
                    await asyncio.sleep(2)
                    await client.send_message("Stickers", packname)
                    await asyncio.sleep(2)
                    await Man.edit(
                        f"**Sticker Berhasil Ditambahkan!**\n         🔥 **[KLIK DISINI](https://t.me/addstickers/{packname})** 🔥\n**Untuk Menggunakan Stickers**"
                    )
                    return
            await client.send_document("stickers", media_)
            await asyncio.sleep(2)
            if (
                await get_response(message, client)
                == "Sorry, the file type is invalid."
            ):
                await Man.edit(
                    "**Gagal Menambahkan Sticker, Gunakan @Stickers Bot Untuk Menambahkan Sticker Anda.**"
                )
                return
            await client.send_message("Stickers", emoji_)
            await asyncio.sleep(2)
            await client.send_message("Stickers", "/done")
        else:
            await Man.edit("`Membuat Sticker Pack Baru`")
            try:
                await client.send_message("Stickers", cmd)
            except YouBlockedUser:
                await client.unblock_user("stickers")
                await client.send_message("stickers", "/addsticker")
            await asyncio.sleep(2)
            await client.send_message("Stickers", packnick)
            await asyncio.sleep(2)
            await client.send_document("stickers", media_)
            await asyncio.sleep(2)
            if (
                await get_response(message, client)
                == "Sorry, the file type is invalid."
            ):
                await Man.edit(
                    "**Gagal Menambahkan Sticker, Gunakan @Stickers Bot Untuk Menambahkan Sticker Anda.**"
                )
                return
            await client.send_message("Stickers", emoji_)
            await asyncio.sleep(2)
            await client.send_message("Stickers", "/publish")
            await asyncio.sleep(2)
            if is_anim:
                await client.send_message("Stickers", f"<{packnick}>")
                await asyncio.sleep(2)
            await client.send_message("Stickers", "/skip")
            await asyncio.sleep(2)
            await client.send_message("Stickers", packname)
            await asyncio.sleep(2)
        await Man.edit(
            f"**Sticker Berhasil Ditambahkan!**\n         🔥 **[KLIK DISINI](https://t.me/addstickers/{packname})** 🔥\n**Untuk Menggunakan Stickers**"
        )
        if os.path.exists(str(media_)):
            os.remove(media_)


async def get_response(message, client):
    return [x async for x in client.get_chat_history("Stickers", limit=1)][0].text


@Client.on_message(filters.command(["packinfo", "stickerinfo"], cmd) & filters.me)
async def packinfo(client: Client, message: Message):
    rep = await edit_or_reply(message, "`Processing...`")
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


@Client.on_message(filters.command("stickers", cmd) & filters.me)
async def cb_sticker(client: Client, message: Message):
    query = get_text(message)
    if not query:
        return await edit_or_reply(message, "**Masukan Nama Sticker Pack!**")
    xx = await edit_or_reply(message, "`Searching sticker packs...`")
    text = requests.get(f"https://combot.org/telegram/stickers?q={query}").text
    soup = bs(text, "lxml")
    results = soup.find_all("div", {"class": "sticker-pack__header"})
    if not results:
        return await xx.edit("**Tidak Dapat Menemukan Sticker Pack 🥺**")
    reply = f"**Keyword Sticker Pack:**\n {query}\n\n**Hasil:**\n"
    for pack in results:
        if pack.button:
            packtitle = (pack.find("div", "sticker-pack__title")).get_text()
            packlink = (pack.a).get("href")
            reply += f" •  [{packtitle}]({packlink})\n"
    await xx.edit(reply)


@Client.on_message(filters.command("tiny", cmd) & filters.me)
async def tinying(client: Client, message: Message):
    reply = message.reply_to_message
    if not (reply and (reply.media)):
        return await edit_or_reply(message, "**Silahkan Balas Ke Pesan Sticker!**")
    Man = await edit_or_reply(message, "`Processing . . .`")
    ik = await client.download_media(reply)
    im1 = Image.open("ProjectMan/resources/blank.png")
    if ik.endswith(".tgs"):
        await client.download_media(reply, "man.tgs")
        await bash("lottie_convert.py man.tgs json.json")
        json = open("json.json", "r")
        jsn = json.read()
        jsn = jsn.replace("512", "2000")
        ("json.json", "w").write(jsn)
        await bash("lottie_convert.py json.json man.tgs")
        file = "man.tgs"
        os.remove("json.json")
    elif ik.endswith((".gif", ".mp4")):
        iik = cv2.VideoCapture(ik)
        busy = iik.read()
        cv2.imwrite("i.png", busy)
        fil = "i.png"
        im = Image.open(fil)
        z, d = im.size
        if z == d:
            xxx, yyy = 200, 200
        else:
            t = z + d
            a = z / t
            b = d / t
            aa = (a * 100) - 50
            bb = (b * 100) - 50
            xxx = 200 + 5 * aa
            yyy = 200 + 5 * bb
        k = im.resize((int(xxx), int(yyy)))
        k.save("k.png", format="PNG", optimize=True)
        im2 = Image.open("k.png")
        back_im = im1.copy()
        back_im.paste(im2, (150, 0))
        back_im.save("o.webp", "WEBP", quality=95)
        file = "o.webp"
        os.remove(fil)
        os.remove("k.png")
    else:
        im = Image.open(ik)
        z, d = im.size
        if z == d:
            xxx, yyy = 200, 200
        else:
            t = z + d
            a = z / t
            b = d / t
            aa = (a * 100) - 50
            bb = (b * 100) - 50
            xxx = 200 + 5 * aa
            yyy = 200 + 5 * bb
        k = im.resize((int(xxx), int(yyy)))
        k.save("k.png", format="PNG", optimize=True)
        im2 = Image.open("k.png")
        back_im = im1.copy()
        back_im.paste(im2, (150, 0))
        back_im.save("o.webp", "WEBP", quality=95)
        file = "o.webp"
        os.remove("k.png")
    await asyncio.gather(
        Man.delete(),
        client.send_sticker(
            message.chat.id,
            sticker=file,
            reply_to_message_id=ReplyCheck(message),
        ),
    )
    os.remove(file)
    os.remove(ik)


@Client.on_message(filters.command(["mmf", "memify"], cmd) & filters.me)
async def memify(client: Client, message: Message):
    if not message.reply_to_message_id:
        await edit_or_reply(message, "**Balas ke pesan foto atau sticker!**")
        return
    reply_message = message.reply_to_message
    if not reply_message.media:
        await edit_or_reply(message, "**Harap Balas ke foto atau sticker!**")
        return
    file = await client.download_media(reply_message)
    Man = await edit_or_reply(message, "`Processing . . .`")
    text = get_arg(message)
    if len(text) < 1:
        return await msg.edit(f"Harap Ketik `{cmd}mmf text`")
    meme = await add_text_img(file, text)
    await asyncio.gather(
        Man.delete(),
        client.send_sticker(
            message.chat.id,
            sticker=meme,
            reply_to_message_id=ReplyCheck(message),
        ),
    )
    os.remove(meme)


@Client.on_message(filters.command(["get", "getsticker", "mtoi"], cmd) & filters.me)
async def stick2png(client: Client, message: Message):
    try:
        await message.edit("`Downloading . . .`")

        path = await message.reply_to_message.download()
        with open(path, "rb") as f:
            content = f.read()
        os.remove(path)

        file_io = BytesIO(content)
        file_io.name = "sticker.png"

        await asyncio.gather(
            message.delete(),
            client.send_photo(
                message.chat.id,
                file_io,
                reply_to_message_id=ReplyCheck(message),
            ),
        )
    except Exception as e:
        return await client.send_message(
            message.chat.id, f"**INFO:** `{e}`", reply_to_message_id=ReplyCheck(message)
        )


add_command_help(
    "sticker",
    [
        [
            f"kang `atau` {cmd}tikel",
            f"Balas {cmd}kang Ke Sticker Atau Gambar Untuk Menambahkan Ke Sticker Pack.",
        ],
        [
            f"kang [emoji] `atau` {cmd}tikel [emoji]",
            f"Untuk Menambahkan dan costum emoji sticker Ke Sticker Pack Mu.\n\n`  •  **NOTE:** Untuk Membuat Sticker Pack baru Gunakan angka dibelakang {cmd}kang\n  •  **CONTOH:** {cmd}kang 2 untuk membuat dan menyimpan ke sticker pack ke 2`",
        ],
        [
            f"packinfo `atau` {cmd}stickerinfo",
            "Untuk Mendapatkan Informasi Sticker Pack.",
        ],
        ["get", "Balas ke sticker untuk mendapatkan foto sticker."],
        ["stickers <nama sticker>", "Untuk Mencari Sticker Pack."],
    ],
)


add_command_help(
    "memify",
    [
        [
            "mmf Teks Atas ; Teks Bawah",
            "Balas Ke Pesan Sticker atau Foto akan Di ubah menjadi sticker teks meme yang di tentukan.",
        ],
    ],
)


add_command_help(
    "tiny",
    [
        [
            "tiny <reply ke foto/sticker>",
            "Untuk Mengubah Sticker Menjadi Kecil.",
        ],
    ],
)
