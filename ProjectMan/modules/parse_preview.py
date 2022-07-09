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
from ProjectMan.utils.sections import section

from .help import add_command_help


@Client.on_message(filters.command("parse", cmd) & filters.me)
async def parse(client: Client, message: Message):
    r = message.reply_to_message
    has_wpp = False
    if not r:
        return await edit_or_reply(message, "Reply to a message with a webpage")
    m_ = await edit_or_reply(message, "`Parsing...`")
    if not r.web_page:
        text = r.text or r.caption
        if text:
            m = await client.send_message("me", text)
            await sleep(1)
            await m.delete()
            if m.web_page:
                r = m
                has_wpp = True
    else:
        has_wpp = True
    if not has_wpp:
        return await m_.edit(
            "Replied message has no webpage preview.",
        )
    wpp = r.web_page
    body = {
        "Title": [wpp.title or "Null"],
        "Description": [(wpp.description[:50] + "...") if wpp.description else "Null"],
        "URL": [wpp.display_url or "Null"],
        "Author": [wpp.author or "Null"],
        "Site Name": [wpp.site_name or "Null"],
        "Type": wpp.type or "Null",
    }
    text = section("Preview", body)
    t = wpp.type
    if t == "Photo":
        media = wpp.photo
        func = client.send_photo
    elif t == "Audio":
        media = wpp.audio
        func = client.send_audio
    elif t == "Video":
        media = wpp.video
        func = client.send_video
    elif t == "Document":
        media = wpp.document
        func = client.send_document
    else:
        media = None
        func = None
    if media and func:
        await m_.delete()
        return await func(
            m_.chat.id,
            media.file_id,
            caption=text,
        )
    await m_.edit(text, disable_web_page_preview=True)


add_command_help(
    "parse",
    [
        [
            "parse",
            "Parse a web_page(link) preview",
        ]
    ],
)
