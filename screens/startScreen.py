from screen import Screen
import PySimpleGUI as sg


class StartScreen(Screen):

    def __init__(self, log):
        self.__log = log

    @property
    def log(self):
        return self.__log

    def start(self, text, menu):
        # layout = [
        #     [sg.Submit(), sg.Exit()]
        # ]

        # window = sg.Window("Start", layout=layout, **self.screen_configs).Finalize()
        # window.Maximize()

        # def func_screen(window):
        #     event, values = window.Read()
        #     if event in (None, 'Exit'):
        #         return False, None
        #     elif event == "Submit":
        #         return False, 
        
        # return self.execute_screen(func_screen, window)
        self.log.info("Starting start screen")
        result = self.get_menu_input(text, menu)
        self.log.info("Finished start screen")
        return result