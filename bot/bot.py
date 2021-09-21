import json

from config import TG_TOKEN
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, messagequeue as mq


def get_info() -> set:
    with open("data/chat_users.json", mode="r", encoding="utf-8") as file:
        invite_users = json.load(file)
    return invite_users


@mq.queuedmessage
def do_send(bot, job) -> None:
    invite_users = get_info()
    for user in invite_users:
        text = "Это тестовое сообщение"
        bot.sendMessage()


def bot():
    bot_send = Bot(
        token=TG_TOKEN,
    )

    updater = Updater(
        bot=bot_send,
    )

    # команда для отправки приглашения на вступление
    command_handler = CommandHandler("send", do_send)
    updater.dispatcher.add_handler(command_handler)

    updater.start_polling()
    updater.idle()



