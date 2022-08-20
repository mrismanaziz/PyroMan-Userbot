#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.
#
# Ported by @mrismanaziz
# FROM File-Sharing-Man < https://github.com/mrismanaziz/File-Sharing-Man/ >
# t.me/Lunatic0de & t.me/SharingUserbot
#

import asyncio
import math

import dotenv
import heroku3
import requests
import urllib3
from pyrogram import Client, filters
from pyrogram.types import Message

from config import *
from ProjectMan.helpers.basic import edit_or_reply
from ProjectMan.helpers.misc import HAPP, in_heroku
from ProjectMan.utils.misc import restart

from .help import add_command_help

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@Client.on_message(filters.command("setvar", CMD_HANDLER) & filters.me)
async def set_var(client: Client, message: Message):
    if len(message.command) < 3:
        return await edit_or_reply(
            message, f"<b>Usage:</b> {CMD_HANDLER}setvar [Var Name] [Var Value]"
        )
    Man = await edit_or_reply(message, "`Processing...`")
    to_set = message.text.split(None, 2)[1].strip()
    value = message.text.split(None, 2)[2].strip()
    if await in_heroku():
        if HAPP is None:
            return await Man.edit(
                "Pastikan HEROKU_API_KEY dan HEROKU_APP_NAME anda dikonfigurasi dengan benar di config vars heroku"
            )
        heroku_config = HAPP.config()
        if to_set in heroku_config:
            await Man.edit(f"Berhasil Mengubah var {to_set} menjadi {value}")
        else:
            await Man.edit(f"Berhasil Menambahkan var {to_set} menjadi {value}")
        heroku_config[to_set] = value
    else:
        path = dotenv.find_dotenv("config.env")
        if not path:
            return await Man.edit(".env file not found.")
        dotenv.set_key(path, to_set, value)
        if dotenv.get_key(path, to_set):
            await Man.edit(f"Berhasil Mengubah var {to_set} menjadi {value}")
        else:
            await Man.edit(f"Berhasil Menambahkan var {to_set} menjadi {value}")
        restart()


@Client.on_message(filters.command("getvar", CMD_HANDLER) & filters.me)
async def varget_(client: Client, message: Message):
    if len(message.command) != 2:
        return await edit_or_reply(
            message, f"<b>Usage:</b> {CMD_HANDLER}getvar [Var Name]"
        )
    Man = await edit_or_reply(message, "`Processing...`")
    check_var = message.text.split(None, 2)[1]
    if await in_heroku():
        if HAPP is None:
            return await Man.edit(
                "Pastikan HEROKU_API_KEY dan HEROKU_APP_NAME anda dikonfigurasi dengan benar di config vars heroku"
            )
        heroku_config = HAPP.config()
        if check_var in heroku_config:
            return await Man.edit(
                f"<b>{check_var}:</b> <code>{heroku_config[check_var]}</code>"
            )
        else:
            return await Man.edit(f"Tidak dapat menemukan var {check_var}")
    else:
        path = dotenv.find_dotenv("config.env")
        if not path:
            return await Man.edit(".env file not found.")
        output = dotenv.get_key(path, check_var)
        if not output:
            await Man.edit(f"Tidak dapat menemukan var {check_var}")
        else:
            return await Man.edit(f"<b>{check_var}:</b> <code>{str(output)}</code>")


@Client.on_message(filters.command("delvar", CMD_HANDLER) & filters.me)
async def vardel_(client: Client, message: Message):
    if len(message.command) != 2:
        return await message.edit(f"<b>Usage:</b> {CMD_HANDLER}delvar [Var Name]")
    Man = await edit_or_reply(message, "`Processing...`")
    check_var = message.text.split(None, 2)[1]
    if await in_heroku():
        if HAPP is None:
            return await Man.edit(
                "Pastikan HEROKU_API_KEY dan HEROKU_APP_NAME anda dikonfigurasi dengan benar di config vars heroku"
            )
        heroku_config = HAPP.config()
        if check_var in heroku_config:
            await message.edit(f"Berhasil Menghapus var {check_var}")
            del heroku_config[check_var]
        else:
            return await message.edit(f"Tidak dapat menemukan var {check_var}")
    else:
        path = dotenv.find_dotenv("config.env")
        if not path:
            return await message.edit(".env file not found.")
        output = dotenv.unset_key(path, check_var)
        if not output[0]:
            return await message.edit(f"Tidak dapat menemukan var {check_var}")
        else:
            await message.edit(f"Berhasil Menghapus var {check_var}")
        restart()


@Client.on_message(filters.command("usage", CMD_HANDLER) & filters.me)
async def usage_heroku(client: Client, message: Message):
    ### Credits CatUserbot
    if await in_heroku():
        if HAPP is None:
            return await message.edit(
                "Pastikan HEROKU_API_KEY dan HEROKU_APP_NAME anda dikonfigurasi dengan benar di config vars heroku"
            )
    else:
        return await edit_or_reply(message, "Only for Heroku Apps")
    dyno = await edit_or_reply(message, "`Checking Heroku Usage. Please Wait...`")
    Heroku = heroku3.from_key(HEROKU_API_KEY)
    account_id = Heroku.account().id
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = "/accounts/" + account_id + "/actions/get-quota"
    r = requests.get("https://api.heroku.com" + path, headers=headers)
    if r.status_code != 200:
        return await dyno.edit("Unable to fetch.")
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)
    day = math.floor(hours / 24)
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)
    await asyncio.sleep(1.5)
    text = f"""
✥ **Informasi Dyno Heroku :**
╔════════════════════╗
 ➠ **Penggunaan Dyno** `{HEROKU_APP_NAME}` :
     •  `{AppHours}`**Jam**  `{AppMinutes}`**Menit |**  [`{AppPercentage}`**%**]
 ➠ **Sisa kuota dyno bulan ini** :
     •  `{hours}`**Jam**  `{minutes}`**Menit |**  [`{percentage}`**%**]
╚════════════════════╝
✥ **Sisa Dyno Heroku** `{day}` **Hari Lagi**"""
    return await dyno.edit(text)


@Client.on_message(filters.command("usange", CMD_HANDLER) & filters.me)
async def usange_heroku(client: Client, message: Message):
    xx = await edit_or_reply(message, "`Processing...`")
    await xx.edit(
        "✥ **Informasi Dyno Heroku :**"
        "\n╔════════════════════╗\n"
        f" ➠ **Penggunaan Dyno** `{HEROKU_APP_NAME}` :\n"
        f"     •  `0`**Jam**  `0`**Menit**  "
        f"**|**  [`0`**%**]"
        "\n◖════════════════════◗\n"
        " ➠ **Sisa kuota dyno bulan ini** :\n"
        f"     •  `1000`**Jam**  `0`**Menit**  "
        f"**|**  [`100`**%**]"
        "\n╚════════════════════╝\n"
    )


add_command_help(
    "heroku",
    [
        ["setvar", "Untuk mengatur variabel config userbot."],
        ["delvar", "Untuk menghapus variabel config userbot."],
        ["getvar", "Untuk melihat variabel config userbot."],
        [
            f"usage atau {CMD_HANDLER}dyno",
            "Untuk mengecheck kouta dyno heroku.",
        ],
        [
            "usange",
            "Fake Usage Kouta Dyno Heroku jadi 1000jam Untuk menipu temanmu wkwk.",
        ],
    ],
)
