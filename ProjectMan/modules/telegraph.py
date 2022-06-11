# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram import Client, filters
from pyrogram.types import Message
from telegraph import Telegraph, upload_file

from config import CMD_HANDLER as cmd
from ProjectMan.helpers.basic import edit_or_reply
from ProjectMan.helpers.tools import *

from .help import *

telegraph = Telegraph()
r = telegraph.create_account(short_name="PyroMan-Userbot")
auth_url = r["auth_url"]


@Client.on_message(filters.command(["tg", "telegraph"], cmd) & filters.me)
async def uptotelegraph(client: Client, message: Message):
    reply = message.reply_to_message
    filesize = 5242880
    Man = await edit_or_reply(message, "`Processing...`")
    # if not replied
    if not reply:
        await Man.edit("`Please reply to media / text...`")
    # replied to text
    elif reply.text:
        if len(reply.text) <= 4096:
            link = telegraph.create_page(
                client.me.first_name,
                html_content=(reply.text.html).replace("\n", "<br>"),
            )
            await Man.edit(
                f"**Berhasil diupload ke [Telegraph](https://telegra.ph/{link.get('path')})**"
            )
        else:
            await Man.edit("The length text exceeds 4096 characters")
    elif reply.media:
        if (
            reply.photo
            and reply.photo.file_size <= filesize
            or reply.video
            and reply.video.file_size <= filesize
            or reply.animation
            and reply.animation.file_size <= filesize
            or reply.sticker
            and reply.sticker.file_size <= filesize
            or reply.document
            and reply.document.file_size <= filesize
        ):
            await Man.edit("`Processing...`")
            if reply.animation or reply.sticker:
                loc = await client.download_media(reply, file_name=f"telegraph.png")
            else:
                loc = await client.download_media(reply)
            try:
                response = upload_file(loc)
            except Exception as e:
                return await Man.edit(f"**ERROR:** `{e}`")
            await Man.edit(
                f"**Berhasil diupload ke [Telegraph](https://telegra.ph{response[0]})**"
            )
            if os.path.exists(loc):
                os.remove(loc)
        else:
            await Man.edit(
                "Please check the file format or file size , it must be less than 5 mb . . ."
            )
    else:
        await Man.edit("Sorry, The File is not supported !")


add_command_help(
    "telegraph",
    [
        [
            f"{cmd}telegraph atau {cmd}tg",
            "Balas ke Pesan Teks atau Media untuk mengunggahnya ke telegraph.",
        ],
    ],
)
