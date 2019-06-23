from telegram.ext import CommandHandler, RegexHandler, CallbackQueryHandler
# from .commands import *
from .thermostat import Thermostat

ts = Thermostat()

dispatches = [
    RegexHandler("TS", ts.ts_menu),
    RegexHandler("get_ts_data", ts.get_data),
]
