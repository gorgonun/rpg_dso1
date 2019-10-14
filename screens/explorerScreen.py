from screen import Screen

class ExplorerScreen(Screen):
    
    def __init__(self, log):
        self.__log = log

    @property
    def log(self):
        return self.__log

    def show_text(self, text):
        self.print_wait_confimation(text)

    def get_action(self, text:str, commands: list):
        output_dict = {
            key: {
                "f": lambda key: key,
                "args": [key]
            }
             for key in commands
             }
        return self.get_adventure_input(text, output_dict)
