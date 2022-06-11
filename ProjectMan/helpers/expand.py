# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import aiohttp


async def expand_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://expandurl.com/api/v1/?url={url}") as resp:
            expanded = await resp.text()

        return expanded if expanded != "false" and expanded[:-1] != url else None
