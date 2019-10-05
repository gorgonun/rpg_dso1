from abc import ABC, abstractmethod

class Place(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @property
    @abstractmethod
    def commands(self):
        return self.__commands.keys()

    @property
    @abstractmethod
    def full_path(self):
        pass

    @property
    def root(self):
        return self.as_list(self.full_path)[0]

    @property
    def top(self):
        return self.as_list(self.full_path)[-1]

    def as_list(self, string: str):
        incomplete_list = list(map(lambda x: [x, "places"], string.split(" ")))
        return [item for sublist in incomplete_list for item in sublist][:-1]
