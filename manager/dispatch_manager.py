import logging

class DispatchManager:
    def __init__(self, dispatcher):
        self.dispatcher = dispatcher

    def add_dispatch(self, dispatches: list):
        for dispatch in dispatches:
            self.dispatcher.add_handler(dispatch)

    def logger(self):
        logging.basicConfig(filename="bot.log",
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.INFO)
        logger = logging.getLogger(__name__)

        def error(bot, update, error):
            logger.warning('Update "%s" caused error "%s"', update, error)

        self.dispatcher.add_error_handler(error)


def add_dispatches(dispatcher: 'updater object', utils_dispatches: list) -> 'created dispatches':
    dm = DispatchManager(dispatcher)

    for dispatches in utils_dispatches:
        dm.add_dispatch(dispatches)

    dm.logger()




