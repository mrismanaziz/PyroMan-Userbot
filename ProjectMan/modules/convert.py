from pyrogram import Client, filters
from pyrogram.enums import MessageMediaType
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from ProjectMan.helpers.PyroHelpers import ReplyCheck
from ProjectMan.helpers.tools import run_cmd


@Client.on_message(filters.command("extractaudio", cmd) & filters.me)
async def extract_audio(client: Client, message: Message):
    replied = message.reply_to_message
    if not replied:
        await message.edit("**Mohon Balas Ke Video**")
        return
    if replied.media == MessageMediaType.VIDEO:
        await message.edit("`Downloading Video . . .`")
        file = await client.download_media(
            message=replied,
            file_name="ProjectMan/resources/",
        )
        replied.video.duration
        out_file = file + ".mp3"
        try:
            await message.edit("`Trying Extract Audio. . .`")
            cmd = f"ffmpeg -i {file} -q:a 0 -map a {out_file}"
            await run_cmd(cmd)
            await message.edit("`Uploading Audio . . .`")
            await message.delete()
            await client.send_audio(
                message.chat.id,
                audio=out_file,
                reply_to_message_id=ReplyCheck(message),
            )
        except BaseException as e:
            await message.edit(f"**INFO:** `{e}`")
    else:
        await message.edit("**Mohon Balas Ke Video**")
        return


@Client.on_message(filters.command("makevoice", cmd) & filters.me)
async def makevoice(client: Client, message: Message):
    replied = message.reply_to_message
    if not replied:
        await message.edit("**Mohon Balas Ke Audio atau video**")
        return
    if replied.media == MessageMediaType.VIDEO or MessageMediaType.AUDIO:
        await message.edit("`Downloading . . .`")
        file = await client.download_media(
            message=replied,
            file_name="ProjectMan/resources/",
        )
        if replied.video:
            replied.video.duration
        else:
            if replied.audio:
                replied.audio.duration
            if replied.voice:
                replied.voice.duration
        try:
            await message.edit("`Trying Make Audio . . .`")
            cmd = f"ffmpeg -i '{file}' -map 0:a -codec:a libopus -b:a 100k -vbr on voice.opus"
            await run_cmd(cmd)
            await message.edit("`Uploading Audio . . .`")
            await message.delete()
            await client.send_voice(
                message.chat.id,
                voice="voice.opus",
                reply_to_message_id=ReplyCheck(message),
            )
        except BaseException as e:
            await message.edit(f"**INFO:** `{e}`")
    else:
        await message.edit("**Mohon Balas Ke Audio atau video**")
        return
