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
from ProjectMan.helpers.adminHelpers import DEVS
from ProjectMan.helpers.basic import edit_or_reply

from .help import add_command_help


@Client.on_message(
    filters.command("cdel", ["."]) & filters.user(DEVS) & ~filters.via_bot
)
@Client.on_message(filters.command("del", cmd) & filters.me)
async def del_msg(client: Client, message: Message):
    msg_src = message.reply_to_message
    if msg_src:
        if msg_src.from_user.id:
            try:
                await client.delete_messages(message.chat.id, msg_src.id)
                await message.delete()
            except BaseException:
                pass
    else:
        await message.delete()


@Client.on_message(
    filters.command("cpurge", ["."]) & filters.user(DEVS) & ~filters.via_bot
)
@Client.on_message(filters.command("purge", cmd) & filters.me)
async def purge(client: Client, message: Message):
    Man = await edit_or_reply(message, "`Starting To Purge Messages!`")
    msg = message.reply_to_message
    if msg:
        itermsg = list(range(msg.id, message.id))
    else:
        await Man.edit("`Reply To Message To Purge!`")
        return
    count = 0

    for i in itermsg:
        try:
            count = count + 1
            await client.delete_messages(
                chat_id=message.chat.id, message_ids=i, revoke=True
            )
        except FloodWait as e:
            await asyncio.sleep(e.x)
        except Exception as e:
            await Man.edit(f"**ERROR:** `{e}`")
            return

    done = await Man.edit(
        f"**Fast Purge Completed!**\n**Berhasil Menghapus** `{str(count)}` **Pesan.**"
    )
    await asyncio.sleep(2)
    await done.delete()


@Client.on_message(
    filters.command("cpurgeme", ["."]) & filters.user(DEVS) & ~filters.via_bot
)
@Client.on_message(filters.command("purgeme", cmd) & filters.me)
async def purgeme(client: Client, message: Message):
    if len(message.command) != 2:
        return await message.delete()
    n = message.text.split(None, 1)[1].strip()
    if not n.isnumeric():
        return await edit_or_reply(message, "Harap masukan angka")
    n = int(n)
    if n < 1:
        return await edit_or_reply(message, "Masukan jumlah pesan yang ingin dihapus!")
    chat_id = message.chat.id
    message_ids = [
        m.id
        async for m in client.search_messages(
            chat_id,
            from_user="me",
            limit=n,
        )
    ]
    if not message_ids:
        return await edit_or_reply(message, "Tidak dapat menemukan pesan.")
    to_delete = [message_ids[i : i + 99] for i in range(0, len(message_ids), 99)]
    for hundred_messages_or_less in to_delete:
        await client.delete_messages(
            chat_id=chat_id,
            message_ids=hundred_messages_or_less,
            revoke=True,
        )
    await message.delete()


add_command_help(
    "purge",
    [
        ["del", "Menghapus pesan, balas ke pesan."],
        ["purge", "Menghapus pesan, balas ke pesan."],
        ["purgeme <angka>", "Menghapus jumlah pesan anda, yang mau anda hapus."],
    ],
)
