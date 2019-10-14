import datetime

class Character:

    def __init__(self, name):
        self.__name = name
        self.__carma = 0
        self.__time_played = datetime.datetime.now()
        self.__key_decisions = []
        self.__dead = False

    @property
    def dead(self):
        return self.__dead

    @dead.setter
    def dead(self, death: bool):
        self.__dead = death

    @property
    def name(self):
        return self.__name

    @property
    def time_played(self):
        return (datetime.datetime.now() - self.__time_played).total_seconds()

    @property
    def carma(self):
        return self.__carma

    @carma.setter
    def carma(self, carma: int):
        self.__carma += carma
    
    @property
    def key_decisions(self):
        return self.__key_decisions
    
    @key_decisions.setter
    def key_decisions(self, key_decision):
        self.__key_decisions.append(key_decision)

    def reset(self):
        self.__carma = 0
        self.__time_played = datetime.datetime.now()
        self.__key_decisions = []
