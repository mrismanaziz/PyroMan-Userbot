# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram import Client, filters
from pyrogram.types import *

from config import CMD_HANDLER as cmd
from ProjectMan.helpers.basic import edit_or_reply

from .help import *

flood = {}


@Client.on_message(filters.command(["block"], cmd) & filters.me)
async def block_user_func(client, message):
    if not message.reply_to_message:
        return await edit_or_reply(message, "Reply to a user's message to block.")
    user_id = message.reply_to_message.from_user.id
    await edit_or_reply(message, "Successfully blocked the user")
    await client.block_user(user_id)


@Client.on_message(filters.command(["unblock"], cmd) & filters.me)
async def unblock_user_func(client, message):
    if not message.reply_to_message:
        return await eor(message, text="Reply to a user's message to unblock.")
    user_id = message.reply_to_message.from_user.id
    await client.unblock_user(user_id)
    await eor(message, "Successfully Unblocked the user")


@Client.on_message(filters.command(["pfp"], cmd) & filters.me)
async def set_pfp(client, message):
    if not message.reply_to_message or not message.reply_to_message.photo:
        return await edit_or_reply(message, "Reply to a photo.")
    photo = await message.reply_to_message.download()
    Man = await edit_or_reply(message, "`Processing...`")
    try:
        await client.set_profile_photo(photo=photo)
        await Man.edit("Successfully Changed PFP.")
    except Exception as e:
        await Man.edit(f"**ERROR:** `{e}`")


@Client.on_message(filters.command(["bio"], cmd) & filters.me)
async def set_bio(client, message):
    Man = await edit_or_reply(message, "`Processing...`")
    if len(message.command) == 1:
        return await Man.edit("Give some text to set as bio.")
    elif len(message.command) > 1:
        bio = message.text.split(None, 1)[1]
        try:
            await client.update_profile(bio=bio)
            await Man.edit("Changed Bio.")
        except Exception as e:
            await Man.edit(f"**ERROR:** `{e}`")
    else:
        return await Man.edit("Give some text to set as bio.")


add_command_help(
    "profile",
    [
        [f"{cmd}bio", "Your Bio Message."],
        [f"{cmd}pfp", "To set Your Profile Pic"],
        [f"{cmd}setpfp", "Reply to any photo to set as pfp."],
        [f"{cmd}vpfp", "View current pfp of user."],
    ],
)
