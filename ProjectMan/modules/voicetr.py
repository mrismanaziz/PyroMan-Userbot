# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import os

from gtts import gTTS
from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from ProjectMan.helpers.basic import edit_or_reply

from .help import add_command_help

lang = "id"  # Default Language for voice


@Client.on_message(filters.me & filters.command(["voice", "tts"], cmd))
async def voice(client: Client, message):
    global lang
    cmd = message.command
    if len(cmd) > 1:
        v_text = " ".join(cmd[1:])
    elif message.reply_to_message and len(cmd) == 1:
        v_text = message.reply_to_message.text
    elif not message.reply_to_message and len(cmd) == 1:
        await edit_or_reply(
            message,
            "**Balas ke pesan atau kirim argumen teks untuk mengonversi ke suara**",
        )
        return
    await client.send_chat_action(message.chat.id, "record_audio")
    # noinspection PyUnboundLocalVariable
    tts = gTTS(v_text, lang=lang)
    tts.save("voice.mp3")
    await message.delete()
    if message.reply_to_message:
        await client.send_voice(
            message.chat.id,
            voice="voice.mp3",
            reply_to_message_id=message.reply_to_message.message_id,
        )
    else:
        await client.send_voice(message.chat.id, voice="voice.mp3")
    await client.send_chat_action(message.chat.id, action="cancel")
    os.remove("voice.mp3")


@Client.on_message(filters.me & filters.command(["voicelang"], cmd))
async def voicelang(client: Client, message: Message):
    global lang
    temp = lang
    lang = message.text.split(None, 1)[1]
    try:
        gTTS("tes", lang=lang)
    except Exception:
        await edit_or_reply(message, "Wrong Language id !")
        lang = temp
        return
    await edit_or_reply(
        message, "**Bahasa untuk Voice Google diganti menjadi** `{}`".format(lang)
    )


add_command_help(
    "voice",
    [
        [f"voice atau {cmd}tts(text)", "Convert text to voice by google."],
        [
            ".voicelang (lang_id) ",
            "Set language of your voice\n\nSome Available Voice lang:"
            "\nID| Language  | ID| Language\n"
            "af: Afrikaans | ar: Arabic\n"
            "cs: Czech     | de: German\n"
            "el: Greek     | en: English\n"
            "es: Spanish   | fr: French\n"
            "hi: Hindi     | id: Indonesian\n"
            "is: Icelandic | it: Italian\n"
            "ja: Japanese  | jw: Javanese\n"
            "ko: Korean    | la: Latin\n"
            "my: Myanmar   | ne: Nepali\n"
            "nl: Dutch     | pt: Portuguese\n"
            "ru: Russian   | su: Sundanese\n"
            "sv: Swedish   | th: Thai\n"
            "tl: Filipino  | tr: Turkish\n"
            "vi: Vietname  |\n"
            "zh-cn: Chinese (Mandarin/China)\n"
            "zh-tw: Chinese (Mandarin/Taiwan)",
        ],
    ],
)
