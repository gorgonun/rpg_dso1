import os
import re
from typing import Callable, Type
from abc import ABC, abstractmethod
import tkinter as tk

class Screen(ABC):
    __root = tk.Tk()
    __os = os.name

    @abstractmethod
    def __init__(self):
        pass

    @property
    def screen_configs(self):
        return {
            "no_titlebar": True,
            "location": (0,0),
            "size": (self.columns, self.rows)
            }

    @property
    @abstractmethod
    def log(self):
        pass

    @property
    def columns(self):
       return self.__root.winfo_screenwidth()

    @property
    def rows(self):
        return self.__root.winfo_screenheight()

    def get_confimation(self):
        input("\nPress enter to continue...")

    def print_wait_confimation(self, text):
        self.print_centralized(text)
        self.get_confimation()

    def get_adventure_input(self, text: str, output_dict: dict, alert: str=None) -> None:
        return self.get_input(text, output_dict, alert)

    def get_menu_input(self, text:str, output_list: list, alert: str=None, text_screen: str= ""):
        output_dict = {str(number): {"f": item[1]} for number, item in zip(range(1, len(output_list) + 1), output_list)}
        options = [x[0] for x in output_list]
        text = text + "\n" + "\n".join(["{}. {}".format(number, option) for number, option in zip(range(1, len(output_dict.keys()) + 1), options)])
        return self.get_input(text, output_dict, alert, help=False, text_screen=text_screen)

    def get_input(self, text: str, output_dict: dict=None, validation_function: Callable[[str], bool]=None, alert: str=None, help: bool=True, help_text: str="", text_screen: str="") -> None:
        self.clear_screen()
        
        if alert:
            self.log.info("Printing alert %s", alert)
            self.print_centralized(alert, space="  ✖  ")
            print("\n")
        
        if text_screen: print(text_screen)
        
        self.print_centralized(text + "\n")
        
        if help and help_text: self.print_centralized(help_text)
        
        user_input = input(">> ")
        self.log.info("Got user input %s", user_input)
        
        if not validation_function:
            result = output_dict.get(user_input)
        else:
            result = validation_function(user_input)
        
        if result and output_dict:
            return self.get_input_result(result)
        elif result:
            return user_input
        
        elif user_input == "?" and help:
            help_text = "► " + "\n► ".join(output_dict.keys())
            return self.get_input(text, output_dict, help_text=help_text)
        
        text_invalid = "Invalid input." + " Write ? to see possible options" if help else "Invalid input."
        return self.get_input(text=text, output_dict=output_dict, validation_function=validation_function, alert=text_invalid, help=help, text_screen=text_screen)

    def get_input_result(self, result_dic: dict=None):
        args = result_dic.get("args")

        if args:
            self.log.info("Args detected for function")
            return result_dic["f"](*args)
        
        self.log.info("Executing function without args")
        return result_dic["f"]()

    def validate_text(self, text: str, allow_empty: bool=False):
        return (allow_empty or len(text) > 0) and re.compile("[a-zA-Z0-9_]*").fullmatch(text)

    def validate_number(self, number: int):
        return re.compile("\d+").fullmatch(number)
    
    def clear_screen(self):
        if self.__os == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def print_centralized(self, text: str, space: str=" "):
        text = self.format_centralized(text, space)
        print(text)

    def format_centralized(self, text: str, space: str=" "):
        text_list = [(line, len(line)) for line in text.split("\n")]
        result_list = []
        for line, length in text_list:
            columns = self.columns - length
            spaces = space * int(int(columns / 2) / len(space))
            result_list.append("{0}{1}{0}".format(spaces, line))
        return "\n".join(result_list)

    def get_variable_input(self, text: str, type_input: Type):
        if type_input == str:
            pattern = re.compile("[a-zA-Z0-9_]*")
        elif type_input == int:
            pattern = re.compile("\d+")
        validation_function = lambda x: pattern.fullmatch(x)
        return self.get_input(text, validation_function=validation_function, help=False)

    def execute_screen(self, func_screen, screen):
        keep = True
        result = None
        while keep:
            execution = func_screen(screen)
            keep, result = execution if execution else (True, None)
        screen.Close()
        return result
