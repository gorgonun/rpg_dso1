from abc import ABC, abstractmethod
import pickle


class Dao(ABC):

    def __init__(self, datasource=""):
        self.__datasource = datasource
        self.object_cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.object_cache, open(self.__datasource, "wb"))

    def __load(self):
        self.object_cache = pickle.load(open(self.__datasource, "rb"))

    def update(self):
        self.__dump()
        self.__load()
