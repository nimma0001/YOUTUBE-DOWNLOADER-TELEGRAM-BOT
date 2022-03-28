#Developer : Hiruwa

from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"📛\n\  (No playlist) Just Send Youtube Url lode."
    await message.reply_text(helptxt)
