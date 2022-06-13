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
from pyrogram.raw import functions
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from ProjectMan.helpers.basic import edit_or_reply

from .help import add_command_help

commands = {
    "ftyping": "typing",
    "fvideo": "record_video",
    "faudio": "record_audio",
    "fround": "record_video_note",
    "fphoto": "upload_photo",
    "fsticker": "choose_sticker",
    "fdocument": "upload_document",
    "flocation": "find_location",
    "fgame": "playing",
    "fcontact": "choose_contact",
    "fstop": "cancel",
    "fscreen": "screenshot",
}


@Client.on_message(filters.command(list(commands), cmd) & filters.me)
async def fakeactions_handler(client: Client, message: Message):
    cmd = message.command[0]
    try:
        sec = int(message.command[1])
        if sec > 60:
            sec = 60
    except:
        sec = None
    await message.delete()
    action = commands[cmd]
    try:
        if action != "screenshot":
            if sec and action != "cancel":
                await client.send_chat_action(chat_id=message.chat.id, action=action)
                await sleep(sec)
            else:
                return await client.send_chat_action(
                    chat_id=message.chat.id, action=action
                )
        else:
            for _ in range(sec if sec else 1):
                await client.send(
                    functions.messages.SendScreenshotNotification(
                        peer=await client.resolve_peer(message.chat.id),
                        reply_to_msg_id=0,
                        random_id=client.rnd_id(),
                    )
                )
                await sleep(0.1)
    except Exception as e:
        return await edit_or_reply(message, f"**ERROR:** `{e}`")


add_command_help(
    "fakeaction",
    [
        [f"{cmd}ftyping [detik]", "Menampilkan Pengetikan Palsu dalam obrolan."],
        [f"{cmd}fgame [detik]", "Menampilkan sedang bermain game Palsu dalam obrolan."],
        [
            f"{cmd}faudio [detik]",
            "Menampilkan tindakan merekam suara palsu dalam obrolan.",
        ],
        [
            f"{cmd}fvideo [detik]",
            "Menampilkan tindakan merekam video palsu dalam obrolan.",
        ],
        [
            f"{cmd}fround [detik]",
            "Menampilkan tindakan merekam video palsu dalam obrolan.",
        ],
        [
            f"{cmd}fphoto [detik]",
            "Menampilkan tindakan mengirim foto palsu dalam obrolan.",
        ],
        [
            f"{cmd}fsticker [detik]",
            "Menampilkan tindakan memilih Sticker palsu dalam obrolan.",
        ],
        [
            f"{cmd}fcontact [detik]",
            "Menampilkan tindakan Share Contact palsu dalam obrolan.",
        ],
        [
            f"{cmd}flocation [detik]",
            "Menampilkan tindakan Share Lokasi palsu dalam obrolan.",
        ],
        [
            f"{cmd}fdocument [detik]",
            "Menampilkan tindakan tengirim Document/File palsu dalam obrolan.",
        ],
        [
            f"{cmd}fscreen [jumlah]",
            "Menampilkan tindakan screenshot palsu. (Gunakan di Obrolan Pribadi)",
        ],
        [f"{cmd}fstop", "Memberhentikan tindakan palsu dalam obrolan."],
    ],
)
