# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio

from pyrogram import *
from pyrogram import filters
from pyrogram.errors import RPCError
from pyrogram.types import *

from config import CMD_HANDLER as cmd
from ProjectMan.helpers.basic import edit_or_reply
from ProjectMan.helpers.PyroHelpers import ReplyCheck
from ProjectMan.utils import extract_user

from .help import add_command_help


@Client.on_message(filters.command(["sg", "sa", "sangmata"], cmd) & filters.me)
async def sg(client: Client, message: Message):
    args = await extract_user(message)
    lol = await edit_or_reply(message, "`Processing...`")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            return await lol.edit(f"`Please specify a valid user!`")
    try:
        await client.send_message("@SangMataInfo_bot", f"/search_id {user.id}")
    except RPCError:
        await client.unblock_user("SangMataInfo_bot")
    await asyncio.sleep(1)
    await client.send_message("@SangMataInfo_bot", f"/search_id {user.id}")
    await asyncio.sleep(1)
    async for opt in client.iter_history("@SangMataInfo_bot", limit=2):
        hmm = opt.text
        if hmm.startswith("Forward"):
            await lol.edit(
                "Bisakah Anda menonaktifkan pengaturan privasi Anda untuk selamanya?"
            )
            return
            await client.read_history("@SangMataInfo_bot")
        if hmm.startswith("No records found"):
            await lol.edit("**Orang Ini Belum Pernah Mengganti Namanya**")
            return
            await client.read_history("@SangMataInfo_bot")
        else:
            await lol.delete()
            await opt.copy(message.chat.id, reply_to_message_id=ReplyCheck(message))


add_command_help(
    "sangmata",
    [
        [
            f"{cmd}sg <reply/userid/username>",
            "Untuk Mendapatkan Riwayat Nama Pengguna selama di telegram.",
        ],
    ],
)
