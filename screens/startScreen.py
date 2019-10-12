from screen import Screen


class StartScreen(Screen):

    def __init__(self, log):
        self.__log = log

    @property
    def log(self):
        return self.__log

    def start(self, text, menu):
        self.log.info("Starting start screen")
        result = self.get_menu_input(text, menu)
        self.log.info("Finished start screen")
        return result