import os
from abc import ABC, abstractmethod

class Screen(ABC):
    __columns, __rows = os.get_terminal_size(1)
    __os = os.name
    
    def get_adventure_input(self, text: str, output_dict: dict, alert: str=None) -> None:
        return self.get_input(text, output_dict, alert)

    def get_menu_input(self, text:str, output_list: list, alert: str=None):
        output_dict = {str(number): item[1] for number, item in zip(range(1, len(output_list) + 1), output_list)}
        options = [x[0] for x in output_list]
        text = text + "\n" + "\n".join(["{}. {}".format(number, option) for number, option in zip(range(1, len(output_dict.keys()) + 1), options)])
        return self.get_input(text, output_dict, alert, help=False)

    def get_input(self, text: str, output_dict: dict, alert: str=None, help=True) -> None:
        try:
            self.clear_screen()
            if alert: self.print_centralized(alert, space="  ✖  ")
            self.print_centralized(text + "\n")
            user_input = input(">> ")
            result = output_dict.get(user_input)
            if result:
                return result()
            elif user_input == "?" and help:
                self.print_centralized("\n► ".join(output_dict.keys()))
                return self.get_menu_input(text, output_dict)
            text_invalid = "Invalid input" + " Write ? to see possible options" if help else "Invalid input"
            return self.get_input(text, output_dict, text_invalid, help=help)
        except KeyboardInterrupt:
            exit()

    def update_terminal_size(self):
        self.__columns, self.__rows = os.get_terminal_size(1)
    
    def clear_screen(self):
        if self.__os == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def print_centralized(self, text: str, space: str=" "):
        text_list = [(line, len(line)) for line in text.split("\n")]
        for line, length in text_list:
            columns = self.__columns - length
            spaces = space * int(int(columns / 2) / len(space))
            print("{0}{1}{0}".format(spaces, line))

            