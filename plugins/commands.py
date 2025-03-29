import asyncio 
from pyrogram import Client, filters, enums
from config import LOG_CHANNEL, API_ID, API_HASH, NEW_REQ_MODE
from plugins.database import db
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

LOG_TEXT = """<b>#NewUser
    
ID - <code>{}</code>

Nᴀᴍᴇ - {}</b>
"""

@Client.on_message(filters.command('start'))
async def start_message(c, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id, m.from_user.first_name)
        await c.send_message(LOG_CHANNEL, LOG_TEXT.format(m.from_user.id, m.from_user.mention))
    
    await m.reply_photo(
        "https://envs.sh/A1q.jpg",
        caption=f"<b>Hello {m.from_user.mention} 👋\n\nI Am Join Request Acceptor Bot. I Can Accept All Old Pending Join Requests.</b>",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton('- Mᴀɪɴ Cʜᴀɴɴᴇʟ -', url='https://t.me/Animes2u')],
                [InlineKeyboardButton('- Oɴɢᴏɪɴɢ Aɴɪᴍᴇ -', url='https://t.me/Animes3u')],
                [InlineKeyboardButton("◇ ᴘᴀɪᴅ ᴘʀᴏᴍᴏᴛɪᴏɴs ◇", url='https://t.me/Animes2u_Professor_Bot')],
                [
                    InlineKeyboardButton("⚡ ᴀʙᴏᴜᴛ ᴍᴇ", callback_data="about"),
                    InlineKeyboardButton("🍁 ᴄʟᴏꜱᴇ", callback_data="close")
                ]
            ]
        )
    )

@Client.on_chat_join_request(filters.group | filters.channel)
async def approve_new(client, m):
    if not NEW_REQ_MODE:
        return 
    try:
        if not await db.is_user_exist(m.from_user.id):
            await db.add_user(m.from_user.id, m.from_user.first_name)
            await client.send_message(LOG_CHANNEL, LOG_TEXT.format(m.from_user.id, m.from_user.mention))
        
        await client.approve_chat_join_request(m.chat.id, m.from_user.id)
        
        try:
            await client.send_photo(
                m.from_user.id,
                "https://envs.sh/A1q.jpg",
                caption=f"<b>Hello {m.from_user.mention} 👋\n\nWelcome To {m.chat.title}\n\nI Am Join Request Acceptor Bot. I Can Accept All Old Pending Join Requests.</b>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton('- Mᴀɪɴ Cʜᴀɴɴᴇʟ -', url='https://t.me/Animes2u')],
                        [InlineKeyboardButton('- Oɴɢᴏɪɴɢ Aɴɪᴍᴇ -', url='https://t.me/Animes3u')],
                        [InlineKeyboardButton("◇ ᴘᴀɪᴅ ᴘʀᴏᴍᴏᴛɪᴏɴs ◇", url='https://t.me/Animes2u_Professor_Bot')],
                        [
                            InlineKeyboardButton("⚡ ᴀʙᴏᴜᴛ ᴍᴇ", callback_data="about"),
                            InlineKeyboardButton("🍁 ᴄʟᴏꜱᴇ", callback_data="close")
                        ]
                    ]
                )
            )
        except Exception as e:
            print(f"Error sending DM: {e}")

    except Exception as e:
        print(f"Error in approve_new: {e}")
