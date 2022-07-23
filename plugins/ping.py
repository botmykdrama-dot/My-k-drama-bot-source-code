import time
from pyrogram import Client, filters
from pyrogram.types.messages_and_media.message import Message

@Client.on_message(filters.command("ping"))
def ping(_, message:Message):
    start_time = int(round(time.time() * 1000))
    reply = message.reply_text("Ping")
    end_time = int(round(time.time() * 1000))
    reply.edit_text(f"Pong\n{end_time - start_time} ms")
