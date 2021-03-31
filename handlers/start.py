from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""I am **{bn}** !!
I let you play music in your group's voice chat 😉
The commands I currently support are:
⚜️ /play - __Plays the replied audio file or YouTube video through link.__
⚜️ /pause - __Pause Voice Chat Music.__
⚜️ /resume - __Resume Voice Chat Music.__
⚜️ /skip - __Skips the current Music Playing In Voice Chat.__
⚜️ /stop - __Clears The Queue as well as ends Voice Chat Music.__
        """,
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
