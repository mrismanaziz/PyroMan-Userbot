# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

from datetime import datetime

from pyrogram import Client, filters
from pyrogram.errors import PeerIdInvalid
from pyrogram.raw import functions
from pyrogram.types import Message, User

from config import CMD_HANDLER as cmd
from ProjectMan.helpers.basic import edit_or_reply
from ProjectMan.helpers.PyroHelpers import ReplyCheck

from .help import add_command_help

WHOIS = (
    "**WHO IS {full_name}?**\n"
    "[Link to profile](tg://user?id={user_id})\n"
    "━━━━━━━━━━━━━━━━\n"
    "**UserID:** `{user_id}`\n"
    "**First Name:** `{first_name}`\n"
    "**Last Name:** `{last_name}`\n"
    "**Username:** `{username}`\n"
    "**Last Online:** `{last_online}`\n"
    "**Common Groups:** `{common_groups}`\n"
    "━━━━━━━━━━━━━━━━\n"
    "**Bio:** {bio}"
)

WHOIS_PIC = (
    "**WHO IS {full_name} ?**\n"
    "[Link to profile](tg://user?id={user_id})\n"
    "━━━━━━━━━━━━━━━━\n"
    "**UserID:** `{user_id}`\n"
    "**First Name:** `{first_name}`\n"
    "**Last Name:** `{last_name}`\n"
    "**Username:** `{username}`\n"
    "**Last Online:** `{last_online}`\n"
    "**Common Groups:** `{common_groups}`\n"
    "━━━━━━━━━━━━━━━━\n"
    "**Profile Pics:** `{profile_pics}`\n"
    "**Last Updated:** `{profile_pic_update}`\n"
    "━━━━━━━━━━━━━━━━\n"
    "**Bio:** {bio}"
)


def LastOnline(user: User):
    if user.is_bot:
        return ""
    elif user.status == "recently":
        return "Recently"
    elif user.status == "within_week":
        return "Within the last week"
    elif user.status == "within_month":
        return "Within the last month"
    elif user.status == "long_time_ago":
        return "A long time ago :("
    elif user.status == "online":
        return "Currently Online"
    elif user.status == "offline":
        return datetime.fromtimestamp(user.last_online_date).strftime(
            "%a, %d %b %Y, %H:%M:%S"
        )


async def GetCommon(bot: Client, get_user):
    common = await bot.send(
        functions.messages.GetCommonChats(
            user_id=await bot.resolve_peer(get_user), max_id=0, limit=0
        )
    )
    return common


def FullName(user: User):
    return user.first_name + " " + user.last_name if user.last_name else user.first_name


def ProfilePicUpdate(user_pic):
    return datetime.fromtimestamp(user_pic[0].date).strftime("%d.%m.%Y, %H:%M:%S")


@Client.on_message(filters.command(["whois", "info"], cmd) & filters.me)
async def who_is(bot: Client, message: Message):
    cmd = message.command
    Man = await edit_or_reply(message, "`Processing...`")
    if not message.reply_to_message and len(cmd) == 1:
        get_user = message.from_user.id
    elif message.reply_to_message and len(cmd) == 1:
        get_user = message.reply_to_message.from_user.id
    elif len(cmd) > 1:
        get_user = cmd[1]
        try:
            get_user = int(cmd[1])
        except ValueError:
            pass
    try:
        user = await bot.get_users(get_user)
    except PeerIdInvalid:
        return await edit_or_reply(message, "I don't know that User.")

    user_details = await bot.get_chat(get_user)
    bio = user_details.bio
    user_pic = await bot.get_profile_photos(user.id)
    pic_count = await bot.get_profile_photos_count(user.id)
    common = await GetCommon(bot, user.id)

    if not user.photo:
        await message.edit(
            WHOIS.format(
                full_name=FullName(user),
                user_id=user.id,
                first_name=user.first_name,
                last_name=user.last_name if user.last_name else "",
                username=user.username if user.username else "",
                last_online=LastOnline(user),
                common_groups=len(common.chats),
                bio=bio if bio else "`No bio set up.`",
            ),
            disable_web_page_preview=True,
        )
    elif user.photo:
        await bot.send_photo(
            message.chat.id,
            user_pic[0].file_id,
            caption=WHOIS_PIC.format(
                full_name=FullName(user),
                user_id=user.id,
                first_name=user.first_name,
                last_name=user.last_name if user.last_name else "",
                username=user.username if user.username else "",
                last_online=LastOnline(user),
                profile_pics=pic_count,
                common_groups=len(common.chats),
                bio=bio if bio else "`No bio set up.`",
                profile_pic_update=ProfilePicUpdate(user_pic),
            ),
            reply_to_message_id=ReplyCheck(message),
        )

        await Man.delete()


add_command_help(
    "whois",
    [
        [
            f"{cmd}whois",
            "Finds out who the person is. Reply to message sent by the person"
            "you want information from and send the command. Without the dot also works.",
        ]
    ],
)
