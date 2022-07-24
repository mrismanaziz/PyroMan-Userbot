from asyncio import gather
from random import choice

from config import CMD_HANDLER as prefixes
from ProjectMan.helpers.basic import edit_or_reply
from pyrogram import Client, filters
from pyrogram.types import Message

from .help import add_command_help


@Client.on_message(filters.command(["asupan", "ptl"], prefixes) & filters.me)
async def asupan_cmd(client: Client, message: Message):
    m = await edit_or_reply(message, "`Tunggu Sebentar...`")
    await gather(
        client.send_video(
            message.chat.id,
            choice(
                [
                    asupan.video.file_id
                    async for asupan in client.search_messages(
                        "tedeasupancache", filter="video"
                    )
                ]
            ),
        ),
        m.delete(),
    )


add_command_help(
    "asupan",
    [
        [
            "asupan or ptl",
            "Untuk Mengirim video asupan secara random.",
        ]
    ],
)
