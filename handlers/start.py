from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os
import sys
from threading import Thread
from pyrogram import idle, filters
from pyrogram.handlers import MessageHandler
from helpers.wrappers import errors, admins_only
from config import BOT_NAME as bn


@Client.on_message(command("start") & other_filters)
async def start_(client: Client, message: Message):
    await message.reply_text(
       f"""🙃 Hi {message.from_user.first_name}!

✨ I am **{bn}** Music Player. 

🥳 I can play music in your Telegram Group's Voice Chat😉
I let you play music in your group's voice chat 😉
The commands I currently support are:
⚜️ /play - __Plays the replied audio file or YouTube video through link.__
⚜️ /pause - __Pause Voice Chat Music.__
⚜️ /resume - __Resume Voice Chat Music.__
⚜️ /skip - __Skips the current Music Playing In Voice Chat.__
⚜️ /stop - __Clears The Queue as well as ends Voice Chat Music.__ 
⚜️ Use these buttons below to know more. 👇""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📔 Source Code 📔", url="https://github.com/jattpawan/evilbot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Group 💬", url="https://t.me/BLAC_USERBOT_GROUP"
                    ),
                    InlineKeyboardButton(
                        "📣 Channel 📣", url="https://t.me/BLAC_USERBOT"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "❌ Close ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
