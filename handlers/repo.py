from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os
import sys
from threading import Thread
from pyrogram import idle, filters
from pyrogram.handlers import MessageHandler
from helpers.wrappers import errors, admins_only
from config import BOT_NAME as bn

@Client.on_message(command("repo") & other_filters)
@errors
async def start(client: Client, message: Message):
    await message.reply_text(
        "**{bn}** if you want musicbot like me then click on repo button to get my repo and click on SESSION button for gernating session and click on heroku botton to deploy me🤍  \n**GO AND DEPLOY ❤️**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💙 REPO 💙", url="https://github.com/jattpawan/evilbot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💚 SESSION 💚", url="https://repl.it/@pawanjatt/evilmusicbot"
                    ),
                    InlineKeyboardButton(
                        "💜 HEROKU 💜", url="https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Fjattpawan%2Fevilbot&template=https%3A%2F%2Fgithub.com%2Fjattpawan%2Fevilbot"
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
    
@Client.on_message(
    filters.command("repo")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        "**{bn}:** if you want musicbot like me then click on repo button to get my repo and click on SESSION button for gernating session and click on heroku botton to deploy me🤍  \n**GO AND DEPLOY ❤️**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💙 REPO 💙", url="https://github.com/jattpawan/evilbot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💚 SESSION 💚", url="https://repl.it/@pawanjatt/evilmusicbot"
                    ),
                    InlineKeyboardButton(
                        "💜 HEROKU 💜", url="https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Fjattpawan%2Fevilbot&template=https%3A%2F%2Fgithub.com%2Fjattpawan%2Fevilbot"
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
