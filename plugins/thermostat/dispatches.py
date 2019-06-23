from telegram.ext import CommandHandler, RegexHandler, CallbackQueryHandler
# from .commands import *
from .thermostat import Thermostat

ts = Thermostat()

dispatches = [
    RegexHandler("TS", ts.ts_menu),
    RegexHandler("Get data from TS", ts.get_data),
]
