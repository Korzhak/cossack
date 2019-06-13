import telegram
from manager.config_parser import Config
from manager.db_manager import manager
from .answers import *

START_STATE = 0
UPDATE_STATE = 1
ERROR_STATE = 2
SUCCESS_STATE = 3
CLEAN_STATE = 4
CLOSE_STATE = 5

VALUE = 4


class Security:
    def __init__(self, chat_id=446819003):
        self.config = Config()

        self.__pin_code = str(manager.get_user(id=chat_id).pin_code)
        self.__pin_counter = 0
        self.__len_pin = len(self.__pin_code)
        self.__matches = 0

    def send_menu(self, bot, update, state=START_STATE):
        if state == START_STATE:
            update.message.reply_text(text=PIN_CODE_TEXT,
                                      reply_markup=telegram.InlineKeyboardMarkup(self.get_keypad()),
                                      parse_mode='HTML')
        elif state == UPDATE_STATE:
            bot.edit_message_text(text=PIN_CODE_TEXT+("*" * self.__pin_counter),
                                  reply_markup=telegram.InlineKeyboardMarkup(self.get_keypad()),
                                  chat_id=update.callback_query.message.chat_id,
                                  message_id=update.callback_query.message.message_id,
                                  parse_mode='HTML')

        elif state == ERROR_STATE:
            bot.edit_message_text(text=PIN_CODE_TEXT + ("*" * self.__pin_counter) + ERROR_TEXT,
                                  reply_markup=telegram.InlineKeyboardMarkup(self.get_keypad()),
                                  chat_id=update.callback_query.message.chat_id,
                                  message_id=update.callback_query.message.message_id,
                                  parse_mode='HTML')

        elif state == SUCCESS_STATE:
            bot.edit_message_text(text=SUCCESS_TEXT,
                                  chat_id=update.callback_query.message.chat_id,
                                  message_id=update.callback_query.message.message_id,
                                  parse_mode='HTML')

        elif state == CLEAN_STATE:
            bot.edit_message_text(text=PIN_CODE_TEXT + CLEAN_FIELD_TEXT,
                                  reply_markup=telegram.InlineKeyboardMarkup(self.get_keypad()),
                                  chat_id=update.callback_query.message.chat_id,
                                  message_id=update.callback_query.message.message_id,
                                  parse_mode='HTML')

        else:
            bot.edit_message_text(text=CLOSE_TEXT,
                                  chat_id=update.callback_query.message.chat_id,
                                  message_id=update.callback_query.message.message_id,
                                  parse_mode='HTML')

    def check_code(self, bot, update):
        data = update.callback_query.data

        if data[:4] == "sec_":
            if data[VALUE] == "<" or data[VALUE] == "x":
                self.__pin_counter = 0
                self.__matches = 0

                if data[VALUE] == "<":
                    self.send_menu(bot, update, CLEAN_STATE)
                elif data[VALUE] == "x":
                    self.send_menu(bot, update, CLOSE_STATE)

            else:
                self.__pin_counter += 1

                if self.__pin_code[self.__pin_counter - 1] == data[VALUE]:
                    self.__matches += 1

                if self.__pin_counter >= self.__len_pin:
                    print("tut")
                    if self.__matches == self.__len_pin:
                        manager.add_session(user_id=update.callback_query.message.chat_id)
                        # self.config.update_config(is_auth=1, last_auth=int(datetime.now().timestamp()))
                        self.send_menu(bot, update, SUCCESS_STATE)
                    else:
                        self.__pin_counter = 0
                        self.__matches = 0
                        self.send_menu(bot, update, ERROR_STATE)
                else:
                    self.send_menu(bot, update, UPDATE_STATE)


    @staticmethod
    def get_keypad():
        keypad = [
            [
                telegram.InlineKeyboardButton(1, callback_data=f'sec_1'),
                telegram.InlineKeyboardButton(2, callback_data=f'sec_2'),
                telegram.InlineKeyboardButton(3, callback_data=f'sec_3'),
            ],
            [
                telegram.InlineKeyboardButton(4, callback_data=f'sec_4'),
                telegram.InlineKeyboardButton(5, callback_data=f'sec_5'),
                telegram.InlineKeyboardButton(6, callback_data=f'sec_6'),
            ],
            [
                telegram.InlineKeyboardButton(7, callback_data=f'sec_7'),
                telegram.InlineKeyboardButton(8, callback_data=f'sec_8'),
                telegram.InlineKeyboardButton(9, callback_data=f'sec_9'),
            ],
            [
                telegram.InlineKeyboardButton("X", callback_data=f'sec_x'),
                telegram.InlineKeyboardButton(0, callback_data=f'sec_0'),
                telegram.InlineKeyboardButton("<-", callback_data=f'sec_<'),
            ],
        ]

        return keypad


def protect_it(func):
    """
    Decorator for protect bot function
    :param func: decorating function
    :return: decorator
    """
    from datetime import datetime

    def wrapper(*args, **kwargs):
        chat_id = args[2].message.chat.id

        security = Security(chat_id)

        # check the duration of the session.
        try:
            start_session = manager.get_last_session().start_session
        except Exception:
            start_session = 0

        try:
            session_duration = manager.get_user(id=chat_id).session_duration
        except Exception:
            session_duration = 1800

        if not ((int(datetime.now().timestamp()) - start_session) >= session_duration):
            func(*args, **kwargs)
        else:
            security.send_menu(*args[1:], **kwargs)

    return wrapper
