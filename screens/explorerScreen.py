from screen import Screen

class ExplorerScreen(Screen):

    def show_text(self, text):
        super().print_wait_confimation(text)

    def get_action(self, text:str, commands: list):
        output_dict = {
            key: {
                "f": lambda key: key,
                "args": [key]
            }
             for key in commands
             }
        return super().get_adventure_input(text, output_dict)