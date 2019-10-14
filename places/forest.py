from place import Place

class Forest(Place):

    def __init__(self):
        self.__name = "forest"
        self.__state = [self.__name]
        self.__states = {
            self.__name: self.format_as_state("move north", new_state=["north"]),
            "north":
                {
                    **self.format_as_state("kill bear", new_state=["north", "nobear"]),
                    **self.format_as_state("go away", next_place="village"),
                    **self.format_as_state("push him away")
                    },
            "nobear":
            {
                **self.format_as_state("steal bag", next_place="village"),
                **self.format_as_state("help woman", next_place="village")
            },
        }

    def move_north(self):
        return self.alter_state("move north")

    def kill_bear(self):
        return self.alter_state("kill bear")

    def go_away(self):
        return self.alter_state("go away")

    def push_him_away(self):
        return self.alter_state("push him away")
    
    def steal_bag(self):
        return self.alter_state("steal bag")

    def help_woman(self):
        return self.alter_state("help woman")

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
