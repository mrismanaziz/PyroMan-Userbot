# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import aiohttp
from yourls import YOURLSClient
from yourls.exceptions import YOURLSKeywordExistsError, YOURLSURLExistsError

YOURLS_URL = None
YOURLS_KEY = None


async def shorten_url(url, keyword):
    if not YOURLS_URL or not YOURLS_KEY:
        return "API ERROR"

    url_checked = await url_check(url)
    if url_checked:
        yourls = YOURLSClient(YOURLS_URL, signature=YOURLS_KEY)
        try:
            shorturl = yourls.shorten(url, keyword).shorturl
            result = shorturl
        except (YOURLSURLExistsError, YOURLSKeywordExistsError):
            result = "KEYWORD/URL Exists"
    else:
        result = "INVALID URL"
    return result


async def url_check(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return resp.status == 200
    except aiohttp.ClientError:
        return False
