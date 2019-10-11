from screens.startScreen import StartScreen
from screens.explorerScreen import ExplorerScreen

class ScreenController():

    def __init__(self, main_controller, log):
        self.__log = log
        self.__explorer_screen = ExplorerScreen(log)
        self.__start_screen = StartScreen(log)
        self.__main_controller = main_controller

    def show_text(self, text: str):
        self.__explorer_screen.show_text(text)

    def get_action(self, text: str, commands: list):
        return self.__explorer_screen.get_action(text, commands)

    def start_screen(self):
        self.__start_screen.start(self)

    def create_character(self):
        pass
    
    def start_game(self):
        self.__log.info("Got signal to start game")
        self.__main_controller.start_game()
