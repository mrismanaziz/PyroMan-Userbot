import asyncio
import datetime
import logging
import os
import re
import sys

from asyncio import sleep
from random import  choice
from pyrogram import SUDOERS, filters
from pyrogram.types import Message
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.input_stream.quality import (HighQualityAudio, HighQualityVideo,
                                                  LowQualityVideo, MediumQualityVideo)
from AnonX import app
from AnonX.utils.inline import queue_back_markup, queue_markup

from AnonX.misc import SUDOERS

logging.basicConfig(level=logging.INFO)

HNDLR = '/'

aud_list = [
    "./AnonX/Audio/AUDIO1",
    "./AnonX/Audio/AUDIO2",
    "./AnonX/Audio/AUDIO3",
    "./AnonX/Audio/AUDIO4",
    "./AnonX/Audio/AUDIO5",
    "./AnonX/Audio/AUDIO6",
    "./AnonX/Audio/AUDIO7",
    "./AnonX/Audio/AUDIO8",
]



@app.on_message(filters.user(SUDOERS) & filters.command(["vcraid"]))
async def vcraid(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    inp = e.text.split(None, 2)[1]
    chat = await Test.get_chat(inp)
    chat_id = chat.id
    aud = choice(aud_list) 

    if inp:
        app = await e.reply_text("**Starting Raid**")
        link = f"https://AnonX.github.io/{aud[1:]}"
        dl = aud
        songname = aud[18:]
        if chat_id in QUEUE:
            pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await Zaid.delete()
            await e.reply_text(f"**> Raiding in:** {chat.title} \n\n**> Audio:** {songname} \n**> Position:** #{pos}")
        else:
import asyncio
import datetime
import logging
import os
import re
import sys

from asyncio import sleep
from random import  choice
from pyrogram import SUDOERS, filters
from pyrogram.types import Message
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.input_stream.quality import (HighQualityAudio, HighQualityVideo,
                                                  LowQualityVideo, MediumQualityVideo)
from AnonX import app
from AnonX.utils.inline import queue_back_markup, queue_markup

from AnonX.misc import SUDOERS

logging.basicConfig(level=logging.INFO)

HNDLR = '/'

aud_list = [
    "./AnonX/Audio/AUDIO1",
    "./AnonX/Audio/AUDIO2",
    "./AnonX/Audio/AUDIO3",
    "./AnonX/Audio/AUDIO4",
    "./AnonX/Audio/AUDIO5",
    "./AnonX/Audio/AUDIO6",
    "./AnonX/Audio/AUDIO7",
    "./AnonX/Audio/AUDIO8",
]



@app.on_message(filters.user(SUDOERS) & filters.command(["vcraid"]))
async def vcraid(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    inp = e.text.split(None, 2)[1]
    chat = await Test.get_chat(inp)
    chat_id = chat.id
    aud = choice(aud_list) 

    if inp:
        app = await e.reply_text("**Starting Raid**")
        link = f"https://AnonX.github.io/{aud[1:]}"
        dl = aud
        songname = aud[18:]
        if chat_id in QUEUE:
            pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await Zaid.delete()
            await e.reply_text(f"**> Raiding in:** {chat.title} \n\n**> Audio:** {songname} \n**> Position:** #{pos}")
        else:
            if call_py:
                await call_py.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py2:
                await call_py2.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py3:
                await call_py3.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py4:
                await call_py4.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py5:
                await call_py5.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await Zaid.delete()
            await e.reply_text(f"**> Raiding in:** {chat.title} \n\n**> Audio:** {songname} \n**> Position:** Ongoing Raid")


@app.on_message(filters.user(SUDOERS) & filters.command(["vraid"]))
async def vraid(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    replied = e.reply_to_message
    inp = e.text.split(None, 2)[1]
    chat = await Test.get_chat(inp)
    chat_id = chat.id
    aud = choice(aud_list) 
    if replied:
        if replied.video or replied.document:
            suhu = await replied.reply("📥 **Downloading Your Replied File...**")
            dl = await replied.download()
    if inp:
        app = await e.reply_text("**Starting Raid**")
        link = f"https://AnonX.github.io/{aud[1:]}"
        songname = aud[18:]
        if chat_id in QUEUE:
            pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await Zaid.delete()
            await e.reply_text(f"**> Raiding in:** {chat.title} \n\n**> Audio:** {songname} \n**> Position:** #{pos}")
        else:
            if call_py:
               await call_py.join_group_call(chat_id, AudioVideoPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py2:
               await call_py2.join_group_call(chat_id, AudioVideoPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py3:
               await call_py3.join_group_call(chat_id, AudioVideoPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py4:
               await call_py4.join_group_call(chat_id, AudioVideoPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py5:
               await call_py5.join_group_call(chat_id, AudioVideoPiped(dl), stream_type=StreamType().pulse_stream)
            add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await Zaid.delete()
            await e.reply_text(f"**> Raiding in:** {chat.title} \n\n**> Video:** {songname} \n**> Position:** Ongoing Raid")


@app.on_message(filters.user(SUDOERS) & filters.command(["raidend"])
async def raidend(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    if gid == uid:
        inp = e.text.split(None, 2)[1]
        chat_ = await Test.get_chat(inp)
        chat_id = chat_.id
    else:
         chat_id = gid
    if chat_id in QUEUE:
        try:
            if call_py:
                await call_py.leave_group_call(chat_id)
            if call_py2:
                await call_py2.leave_group_call(chat_id)
            if call_py3:
                await call_py3.leave_group_call(chat_id)
            if call_py4:
                await call_py4.leave_group_call(chat_id)
            if call_py5:
                await call_py5.leave_group_call(chat_id)
            await e.reply_text("**VC Raid Ended!**")
        except Exception as ex:
            await e.reply_text(f"**ERROR** \n`{ex}`")
    else:
        await e.reply_text("**No ongoing raid!**")￼Enter            if call_py:
                await call_py.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py2:
                await call_py2.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py3:
                await call_py3.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py4:
                await call_py4.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py5:
                await call_py5.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await Zaid.delete()
            await e.reply_text(f"**> Raiding in:** {chat.title} \n\n**> Audio:** {songname} \n**> Position:** Ongoing Raid")


@app.on_message(filters.user(SUDOERS) & filters.command(["vraid"]))
async def vraid(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    replied = e.reply_to_message
    inp = e.text.split(None, 2)[1]
    chat = await Test.get_chat(inp)
    chat_id = chat.id
    aud = choice(aud_list) 
    if replied:
        if replied.video or replied.document:
      suhu = await replied.reply("📥 **Downloading Your Replied File...**")
            dl = await replied.download()
    if inp:
        app = await e.reply_text("**Starting Raid**")
        link = f"https://AnonX.github.io/{aud[1:]}"
        songname = aud[18:]
        if chat_id in QUEUE:
            pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await Zaid.delete()
            await e.reply_text(f"**> Raiding in:** {chat.title} \n\n**> Audio:** {songname} \n**> Position:** #{pos}")
        else:
            if call_py:
               await call_py.join_group_call(chat_id, AudioVideoPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py2:
               await call_py2.join_group_call(chat_id, AudioVideoPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py3:
               await call_py3.join_group_call(chat_id, AudioVideoPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py4:
               await call_py4.join_group_call(chat_id, AudioVideoPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py5:
               await call_py5.join_group_call(chat_id, AudioVideoPiped(dl), stream_type=StreamType().pulse_stream)
            add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await Zaid.delete()
            await e.reply_text(f"**> Raiding in:** {chat.title} \n\n**> Video:** {songname} \n**> Position:** Ongoing Raid")


