import asyncio
from pyrogram import Client, filters
from testing import app

@app.on_message(
    filters.command(["restart"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def restart(client: Client, message: Message):
    reply = await message.reply_text("ʀᴇꜱᴛᴀʀᴛɪɴɢ...")
    await message.delete()
    await reply.edit_text("ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ʀᴇꜱᴛᴀʀᴛᴇᴅ ʙᴀᴅᴜꜱᴇʀʙᴏᴛ...\n\n💞 ᴡᴀɪᴛ 1-2 ᴍɪɴᴜᴛᴇꜱ\nʟᴏᴀᴅ ᴘʟᴜɢɪɴꜱ...</b>")
    os.system(f"kill -9 {os.getpid()} && python3 -m YukkiMusic")

#sudo
