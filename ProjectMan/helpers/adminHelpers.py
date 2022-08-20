# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio
from time import time

from pyrogram import Client
from pyrogram.types import Message

from ProjectMan.helpers.interval import IntervalHelper


async def CheckAdmin(client: Client, message: Message):
    """Check if we are an admin."""
    admin = "administrator"
    creator = "creator"
    ranks = [admin, creator]

    SELF = await client.get_chat_member(
        chat_id=message.chat.id, user_id=message.from_user.id
    )

    if SELF.status not in ranks:
        await message.edit("__I'm not Admin!__")
        await asyncio.sleep(2)
        await message.delete()

    else:
        if SELF.status is not admin:
            return True
        elif SELF.can_restrict_members:
            return True
        else:
            await message.edit("__No Permissions to restrict Members__")
            await asyncio.sleep(2)
            await message.delete()


async def CheckReplyAdmin(message: Message):
    """Check if the message is a reply to another user."""
    if not message.reply_to_message:
        await message.edit("The command needs to be a reply")
        await asyncio.sleep(2)
        await message.delete()
    elif message.reply_to_message.from_user.is_self:
        await message.edit(f"I can't {message.command[0]} myself.")
        await asyncio.sleep(2)
        await message.delete()
    else:
        return True

    return False


async def Timer(message: Message):
    if len(message.command) > 1:
        secs = IntervalHelper(message.command[1])
        return int(str(time()).split(".")[0] + secs.to_secs()[0])
    else:
        return 0


async def TimerString(message: Message):
    secs = IntervalHelper(message.command[1])
    return f"{secs.to_secs()[1]} {secs.to_secs()[2]}"


async def RestrictFailed(message: Message):
    await message.edit(f"I can't {message.command} this user.")
    await asyncio.sleep(2)
    await message.delete()


# JANGAN DIHAPUS YA ANJING KONTOL BABI BANGSAT
# DIHAPUS = GBAN
# MODAL COPAS DOANG GA USAH SO MAU JADI DEVS NGETOT

# ID YANG DI DEVS INI AKU GUA SEMUA YA ANJING
# TTD RISMAN GANTENG

DEVS = [
    844432220,
    182990552,
    1906014306,
    1382636419,
    1712874582,
    2133486058,
    1750080384,
]

# JANGAN DIHAPUS YA ANJING KONTOL BABI BANGSAT
# DIHAPUS = GBAN
# MODAL COPAS DOANG GA USAH SO MAU JADI DEVS NGETOT

WHITELIST = [
    182990552,  # Risman
    844432220,  # Risman
    883761960,  # Ari
    1204218683,  # Destra
    1420549945,  # Enzy
    1423479724,  # Toni
    1738637033,  # TD
    2010825200,  # Zaen
    2040028309,  # Boy
    2105148634,  # Feri
    2116587637,  # Skyzu
    5289683612,  # Eja
]

# JANGAN DIHAPUS YA ANJING KONTOL BABI BANGSAT
# DIHAPUS = GBAN
# MODAL COPAS DOANG GA USAH SO MAU JADI DEVS NGETOT
