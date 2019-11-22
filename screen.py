import os
import re
from abc import ABC, abstractmethod
import tkinter as tk
import math

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

    def centralize(self, rows=1, columns=0.8):
        return {"size": (math.floor(self.columns * columns), rows), "pad": (math.floor(self.columns * (1 - columns)), 0)}

    def validate_text(self, text: str, allow_empty: bool=False):
        return (allow_empty or len(text) > 0) and re.compile("[a-zA-Z0-9_]*").fullmatch(text)

    def validate_number(self, number: int):
        return re.compile("\d+").fullmatch(number)

    def execute_screen(self, func_screen, screen, *args):
        keep = True
        result = None
        while keep:
            execution = func_screen(screen, *args)
            keep, result = execution if execution else (True, None)
        screen.Close()
        return result
