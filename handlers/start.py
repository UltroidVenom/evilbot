from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""I am **{bn}** !!
I let you play music in your group's voice chat 😉
Don't Forget to add my assistant in your group
Don't Forget To Make Admin Me And My assistant With Manage Voice Chat Permission
The commands I currently support are:
⚜️ /play - __Plays the replied audio file or YouTube video through link.__
⚜️ /pause - __Pause Voice Chat Music.__
⚜️ /resume - __Resume Voice Chat Music.__
⚜️ /skip - __Skips the current Music Playing In Voice Chat.__
⚜️ /end - __Clears The Queue as well as ends Voice Chat Music.__
⚜️ /play (song name) - __Play Song Directly From YouTube
               """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Add ʋɛռօʍ ʍʊֆɨƈ ɮօȶ to your group", url="t.me/{}?startgroup=true".format(context.bot.username)
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Group 💬", url="https://t.me/CrackMonkeyChats"
                    ),
                    InlineKeyboardButton(
                        "📣 Channel 📣", url="https://t.me/CrackMonkey"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ʍʏ ʍǟֆȶɛʀ", url="https://t.me/R2K_VENOM"
                    )
                ]
            ]
        )
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**🔴 Music player is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎙️ Support Group 🎙️", url="https://t.me/CrackMonkeyChats")
                ]
            ]
        )
   )


