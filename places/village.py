from place import Place

class Village(Place):

    def __init__(self):
        self.__name = "village"
        self.__state = [self.__name]
        self.__states = {self.__name: self.format_as_state("walk away")}

    def walk_away(self):
        return self.alter_state("walk away")

    @property
    def name(self):
        return self.__name

    @property
    def state(self):
        return self.__state[-1]

    @state.setter
    def state(self, new_state: str):
        self.__state = new_state

    @property
    def complete_state(self):
        return self.__state

    @property
    def states(self):
        return self.__states

    @property
    def commands(self):
        return self.__states[self.state].keys()

