import asyncio
from CakeMusic import *
from CakeMusic.plugins.Play import *
from CakeMusic import app
from pyrogram import Client, filters as pyrofl
from config import MONGO_DB_URL, OWNER_ID
from CakeMusic.misc import SUDOERS
from pyrogram.types import Message

@app.on_message(cdx(["pause", "vpause"]) & ~pyrofl.private)
async def restart(client: Client, message: Message):
    reply = await message.reply_text("ʀᴇꜱᴛᴀʀᴛɪɴɢ...")
    await message.delete()
    await reply.edit_text("ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ʀᴇꜱᴛᴀʀᴛᴇᴅ ʙᴏᴛ...\n\n💞 ᴡᴀɪᴛ 1-2 ᴍɪɴᴜᴛᴇꜱ\nʟᴏᴀᴅ ᴘʟᴜɢɪɴꜱ...</b>")
    os.system(f"kill -9 {os.getpid()} && python3 -m CakeMusic")
