from screen import Screen


class StartScreen(Screen):

    def __init__(self, log):
        self.__log = log
    
    def start(self, controller):
        self.log.info("Starting start screen")
        text = "Start menu"
        start = lambda: controller.start_game()
        create = lambda: controller.create_character()
        menu = [("Start game", start), ("Create character", create), ("Exit", exit)]
        self.get_menu_input(text, menu)
        self.log.info("Finished")

    @property
    def log(self):
        return self.__log