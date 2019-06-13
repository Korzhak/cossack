from telegram.ext import CommandHandler, RegexHandler
from .commands import *
from .home import Home

home = Home()

dispatches = [
    CommandHandler(START_COMMAND, home.home_menu),
    CommandHandler(GET_ID, home.get_my_id),
    RegexHandler(BACK_TO_HOME, home.home_menu),
    RegexHandler(ABOUT_OS, home.about_os),
]