from screen import Screen
import PySimpleGUI as sg


class StartScreen(Screen):

    def __init__(self, log):
        self.__log = log

    @property
    def log(self):
        return self.__log

    def start(self):
        layout = [
            [sg.Button("Start game", key="start", **self.centralize())],
            [sg.Button("Player manager", key="manager", **self.centralize())],
            [sg.Button("Show ranking", key="ranking", **self.centralize())],
            [sg.Button("Exit", **self.centralize())]
        ]

        window = sg.Window("Start", layout=layout, **self.screen_configs).Finalize()
        window.Maximize()

        def func_screen(window):
            event, values = window.Read()
            if event in (None, 'Exit'):
                return False, None
            else:
                return False, event
        
        return self.execute_screen(func_screen, window)
