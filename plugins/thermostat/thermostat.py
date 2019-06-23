import telegram
from .thermostat_manager import ThermostatBox

class Thermostat:
    def __init__(self):
        self.ts = ThermostatBox()

        self.custom_keyboard = [
            ["Get data from TS"],
            ["Back to home"]
        ]

    def ts_menu(self, bot, update):
        reply_markup = telegram.ReplyKeyboardMarkup(self.custom_keyboard)
        bot.send_message(chat_id=update.message.chat_id,
                         text="Thermostat-box managing",
                         reply_markup=reply_markup)

    def get_data(self, bot, update):
        text = self.ts.get_data_from_box()
        formatting_text = f"Thermostat: {'On' if int(text[0]) else 'Off'}\n" \
                          f"Current state: {text[1]}\n" \
                          f"Temperature: {text[2]}\n" \
                          f"Set temp.: {text[3]}\n" \
                          f"Light: {'On' if int(text[6]) else 'Off'}\n"
        bot.send_message(chat_id=update.message.chat_id,
                         text=formatting_text, parse_mode="HTML")
