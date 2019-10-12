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

    def start_screen(self, text, menu):
        return self.__start_screen.start(text, menu)

    def create_character(self):
        pass

