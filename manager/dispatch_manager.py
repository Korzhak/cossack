

class DispatchManager:
    def __init__(self, dispatcher):
        self.dispatcher = dispatcher

    def add_dispatch(self, dispatches: list):
        for dispatch in dispatches:
            self.dispatcher.add_handler(dispatch)


def add_dispatches(dispatcher: 'updater object', utils_dispatches: list) -> 'created dispatches':
    dm = DispatchManager(dispatcher)

    for dispatches in utils_dispatches:
        dm.add_dispatch(dispatches)



