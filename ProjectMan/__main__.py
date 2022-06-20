# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import importlib

from pyrogram import idle
from uvloop import install

from config import *
from ProjectMan import BOTLOG_CHATID, LOGGER, LOOP, bots
from ProjectMan.helpers.misc import git, heroku
from ProjectMan.modules import ALL_MODULES

MSG_ON = """
🔥 **PyroMan-Userbot Berhasil Di Aktifkan**
━━
➠ **Userbot Version -** `{}`
➠ **Ketik** `{}alive` **untuk Mengecheck Bot**
━━
"""


async def main():
    for all_module in ALL_MODULES:
        importlib.import_module(f"ProjectMan.modules.{all_module}")
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("Lunatic0de")
            await bot.join_chat("SharingUserbot")
            await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER))
        except Exception as a:
            LOGGER("main").warning(a)
    await idle()


if __name__ == "__main__":
    LOGGER("ProjectMan").info("Starting PyroMan-UserBot")
    LOGGER("ProjectMan").info(f"Total Clients = {len(bots)} Users")
    install()
    git()
    heroku()
    LOGGER("ProjectMan").info(f"PyroMan-UserBot v{BOT_VER} [🔥 BERHASIL DIAKTIFKAN! 🔥]")
    LOOP.run_until_complete(main())
