# -*-codding: utf-8-*-

from telegram.ext import Updater
from .config_parser import Config
from .dispatch_manager import add_dispatches


config = Config()

updater = Updater(token=config.bot.token)
dispatcher = updater.dispatcher


def run(utils_dispatches):
    add_dispatches(dispatcher, utils_dispatches)
    updater.start_polling()
    updater.idle()
