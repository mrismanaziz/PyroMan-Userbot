# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram import Client, filters
from pyrogram.types import ChatPermissions, Message

from config import CMD_HANDLER as cmd
from ProjectMan import *
from ProjectMan.helpers.adminHelpers import DEVS
from ProjectMan.helpers.basic import edit_or_reply
from ProjectMan.helpers.PyroHelpers import get_ub_chats
from ProjectMan.utils import extract_user

from .help import add_command_help


def globals_init():
    try:
        global sql, sql2
        from importlib import import_module

        sql = import_module("ProjectMan.helpers.SQL.gban_sql")
        sql2 = import_module("ProjectMan.helpers.SQL.gmute_sql")
    except Exception as e:
        sql = None
        sql2 = None
        LOGS.warn("Unable to run GBan and GMute command, no SQL connection found")
        raise e


globals_init()


@Client.on_message(
    filters.command("cgban", ["."]) & filters.user(DEVS) & ~filters.via_bot
)
@Client.on_message(filters.command("gban", cmd) & filters.me)
async def gban_user(client: Client, message: Message):
    args = await extract_user(message)
    reply = message.reply_to_message
    if message.from_user.id != client.me.id:
        Man = await message.reply("`Gbanning...`")
    else:
        Man = await message.edit("`Gbanning....`")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            return await Man.edit("`Please specify a valid user!`")
    elif reply:
        user_id = reply.from_user.id
        user = await client.get_users(user_id)
    else:
        return await Man.edit("`Please specify a valid user!`")

    try:
        replied_user = reply.from_user
        if replied_user.is_self:
            return await Man.edit("**ngapain ngegban diri sendiri goblok 🐽**")
    except BaseException:
        pass

    if sql.is_gbanned(user.id):
        return await Man.edit(
            f"[Jamet](tg://user?id={user.id}) **ini sudah ada di daftar gbanned**"
        )
    f_chats = await get_ub_chats(client)
    if not f_chats:
        return await Man.edit("**Anda tidak mempunyai GC yang anda admin 🥺**")
    er = 0
    done = 0
    for gokid in f_chats:
        try:
            await client.ban_chat_member(chat_id=gokid, user_id=int(user.id))
            done += 1
        except BaseException:
            er += 1
    sql.gban(user.id)
    await Man.edit(
        r"**\\#GBanned_User//**"
        f"\n\n**First Name:** [{user.first_name}](tg://user?id={user.id})"
        f"\n**User ID:** `{user.id}`"
        f"\n**Affected To:** `{done}` **Chats**"
    )


@Client.on_message(
    filters.command("cungban", ["."]) & filters.user(DEVS) & ~filters.via_bot
)
@Client.on_message(filters.command("ungban", cmd) & filters.me)
async def ungban_user(client: Client, message: Message):
    args = await extract_user(message)
    reply = message.reply_to_message
    if message.from_user.id != client.me.id:
        Man = await message.reply("`UnGbanning...`")
    else:
        Man = await message.edit("`UnGbanning....`")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            await Man.edit(f"`Please specify a valid user!`")
            return
    elif reply:
        user_id = reply.from_user.id
        user = await client.get_users(user_id)
    else:
        await Man.edit(f"`Please specify a valid user!`")
        return

    try:
        replied_user = reply.from_user
        if replied_user.is_self:
            return await Man.edit("**ngapain ngeungban diri sendiri goblok 🐽**")
    except BaseException:
        pass

    try:
        if not sql.is_gbanned(user.id):
            return await Man.edit("`User already ungban`")
        ung_chats = await get_ub_chats(client)
        if not ung_chats:
            return await Man.edit("`No Chats to unGban!`")
        er = 0
        done = 0
        for good_boi in ung_chats:
            try:
                await client.unban_chat_member(chat_id=good_boi, user_id=user.id)
                done += 1
            except BaseException:
                er += 1
        sql.ungban(user.id)
        await Man.edit(
            r"**\\#UnGbanned_User//**"
            f"\n\n**First Name:** [{user.first_name}](tg://user?id={user.id})"
            f"\n**User ID:** `{user.id}`"
            f"\n**Affected To:** `{done}` **Chats**"
        )
    except Exception as e:
        await Man.edit(f"**ERROR:** `{e}`")
        return


@Client.on_message(filters.command("listgban", cmd) & filters.me)
async def gbanlist(client: Client, message: Message):
    users = sql.gbanned_users()
    Man = await edit_or_reply(message, "`Processing...`")
    if not users:
        return await Man.edit("The list is empty!")
    gban_list = "**GBanned Users:**\n"
    count = 0
    for i in users:
        count += 1
        gban_list += f"**{count} -** `{i.sender}`\n"
    return await Man.edit(gban_list)


@Client.on_message(filters.command("gmute", cmd) & filters.me)
async def gmute_user(client: Client, message: Message):
    args = await extract_user(message)
    reply = message.reply_to_message
    Man = await edit_or_reply(message, "`Processing...`")
    if len(args):
        try:
            user = await client.get_users(args)
        except Exception:
            await Man.edit(f"`Please specify a valid user!`")
            return
    elif reply:
        user_id = reply.from_user.id
        user = await client.get_users(user_id)
    else:
        await Man.edit(f"`Please specify a valid user!`")
        return

    try:
        replied_user = reply.from_user
        if replied_user.is_self:
            return await Man.edit("`Calm down anybob, you can't gmute yourself.`")
    except BaseException:
        pass

    try:
        if sql2.is_gmuted(user.id):
            return await Man.edit("`User already gmuted`")
        sql2.gmute(user.id)
        await Man.edit(f"[{user.first_name}](tg://user?id={user.id}) globally gmuted!")
        try:
            common_chats = await client.get_common_chats(user.id)
            for i in common_chats:
                await i.restrict_member(user.id, ChatPermissions())
        except BaseException:
            pass
    except Exception as e:
        await Man.edit(f"**ERROR:** `{e}`")
        return


@Client.on_message(filters.command("ungmute", cmd) & filters.me)
async def ungmute_user(client: Client, message: Message):
    args = await extract_user(message)
    reply = message.reply_to_message
    Man = await edit_or_reply(message, "`Processing...`")
    if len(args):
        try:
            user = await client.get_users(args)
        except Exception:
            await Man.edit(f"`Please specify a valid user!`")
            return
    elif reply:
        user_id = reply.from_user.id
        user = await client.get_users(user_id)
    else:
        await Man.edit(f"`Please specify a valid user!`")
        return

    try:
        replied_user = reply.from_user
        if replied_user.is_self:
            return await Man.edit("`Calm down anybob, you can't ungmute yourself.`")
    except BaseException:
        pass

    try:
        if not sql2.is_gmuted(user.id):
            return await Man.edit("`User already ungmuted`")
        sql2.ungmute(user.id)
        try:
            common_chats = await client.get_common_chats(user.id)
            for i in common_chats:
                await i.unban_member(user.id)
        except BaseException:
            pass
        await Man.edit(
            f"[{user.first_name}](tg://user?id={user.id}) globally ungmuted!"
        )
    except Exception as e:
        await Man.edit(f"**ERROR:** `{e}`")
        return


@Client.on_message(filters.command("listgmute", cmd) & filters.me)
async def gmutelist(client: Client, message: Message):
    users = sql2.gmuted_users()
    Man = await edit_or_reply(message, "`Processing...`")
    if not users:
        return await Man.edit("listEmpty")
    gmute_list = "**GMuted Users:**\n"
    count = 0
    for i in users:
        count += 1
        gmute_list += f"**{count} -** `{i.sender}`\n"
    return await Man.edit(gmute_list)


@Client.on_message(filters.me, filters.incoming, group=69)
async def gban_check(client: Client, message: Message):
    if sql.is_gbanned(message.from_user.id):
        try:
            user_id = message.from_user.id
            chat_id = message.chat.id
            await client.ban_chat_member(chat_id, user_id)
        except BaseException:
            pass

    message.continue_propagation()


@Client.on_message(filters.me, filters.incoming, group=69)
async def gmute_check(client: Client, message: Message):
    if sql2.is_gmuted(message.from_user.id):
        await message.delete()
        try:
            user_id = message.from_user.id
            chat_id = message.chat.id
            await client.restrict_chat_member(chat_id, user_id, ChatPermissions())
        except BaseException:
            pass

    message.continue_propagation()


add_command_help(
    "globals",
    [
        [
            f"{cmd}gban <reply/username/userid>",
            "Melakukan Global Banned Ke Semua Grup Dimana anda Sebagai Admin.",
        ],
        [f"{cmd}ungban <reply/username/userid>", "Membatalkan Global Banned."],
        [f"{cmd}listgban", "Menampilkan List Global Banned."],
    ],
)
