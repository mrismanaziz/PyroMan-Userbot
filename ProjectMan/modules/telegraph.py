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
from telegraph import Telegraph, exceptions, upload_file

from config import CMD_HANDLER as cmd
from ProjectMan.helpers.basic import edit_or_reply, get_text
from ProjectMan.helpers.tools import *

from .help import *

telegraph = Telegraph()
r = telegraph.create_account(short_name="PyroMan-Userbot")
auth_url = r["auth_url"]


@Client.on_message(filters.command(["tg", "telegraph"], cmd) & filters.me)
async def uptotelegraph(client: Client, message: Message):
    Man = await edit_or_reply(message, "`Processing . . .`")
    if not message.reply_to_message:
        await Man.edit(
            "**Mohon Balas Ke Pesan, Untuk Mendapatkan Link dari Telegraph.**"
        )
        return
    if message.reply_to_message.media:
        if message.reply_to_message.sticker:
            m_d = await convert_to_image(message, client)
        else:
            m_d = await message.reply_to_message.download()
        try:
            media_url = upload_file(m_d)
        except exceptions.TelegraphException as exc:
            await Man.edit(f"**ERROR:** `{exc}`")
            os.remove(m_d)
            return
        U_done = (
            f"**Berhasil diupload ke** [Telegraph](https://telegra.ph/{media_url[0]})"
        )
        await Man.edit(U_done)
        os.remove(m_d)
    elif message.reply_to_message.text:
        page_title = get_text(message) if get_text(message) else client.me.first_name
        page_text = message.reply_to_message.text
        page_text = page_text.replace("\n", "<br>")
        try:
            response = telegraph.create_page(page_title, html_content=page_text)
        except exceptions.TelegraphException as exc:
            await Man.edit(f"**ERROR:** `{exc}`")
            return
        wow_graph = f"**Berhasil diupload ke** [Telegraph](https://telegra.ph/{response['path']})"
        await Man.edit(wow_graph)


add_command_help(
    "telegraph",
    [
        [
            f"telegraph atau {cmd}tg",
            "Balas ke Pesan Teks atau Media untuk mengunggahnya ke telegraph.",
        ],
    ],
)
