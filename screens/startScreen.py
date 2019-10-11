from screen import Screen


class StartScreen(Screen):

    def __init__(self, log):
        self.__log = log

    @property
    def log(self):
        return self.__log

    def start(self):
        self.log.info("Starting start screen")
        text = "Start menu"
        start = lambda: "start_game"
        create = lambda: "create_character"
        menu = [("Start game", start), ("Create character", create), ("Exit", exit)]
        result = self.get_menu_input(text, menu)
        self.log.info("Finished start screen")
        return result