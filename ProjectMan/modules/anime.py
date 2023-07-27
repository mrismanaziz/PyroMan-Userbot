import requests
from pyrogram import Client, filters
from pyrogram.types import Message

# Assuming you have defined your bot and its CMD_HANDLER in config.py
from config import CMD_HANDLER as cmd

API_URL = "https://api.nekosapi.com/v2/images/random"


@Client.on_message(filters.command("randomanime", cmd) & filters.me)
async def random_anime(client: Client, message: Message):
    # Send the "Processing..." message
    await message.edit("Fetching a random anime image...")

    # Make the API request
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()["data"]["attributes"]
        image_url = data["file"]
        title = data["title"]
    except (requests.exceptions.RequestException, KeyError):
        await message.edit("Failed to fetch a random anime image.")
        return

    # Send the image and title as a reply
    await client.send_photo(message.chat.id, image_url, caption=f"**Title:** {title}")

    # Edit the original message to indicate success
    await message.edit("Random anime image sent!")
