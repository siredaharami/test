from pyrogram import Client, filters
import time
from CakeMusic import app

# Ping Command
@app.on_message(filters.command("ping", prefixes=["."]) & filters.me)
async def ping(client, message):
    start_time = time.time()
    reply = await message.reply_text("Pinging...")
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000)  # Convert to ms
    await reply.edit_text(f"Pong! 🏓\nPing: {ping_time} ms")
