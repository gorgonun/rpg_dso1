from abc import ABC, abstractmethod

class Place(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @property
    @abstractmethod
    def commands(self):
        pass

    @property
    def full_path(self):
        return self.root + " " + self.complete_state

    @property
    @abstractmethod
    def state(self):
        pass
    
    @state.setter
    @abstractmethod
    def state(self, new_state):
        pass

    @property
    @abstractmethod
    def states(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    def root(self):
        return self.stage

    @property
    def top(self):
        return self.as_list(self.full_path)[-1]

    def as_list(self, string: str):
        incomplete_list = list(map(lambda x: [x, "places"], string.split(" ")))
        return [item for sublist in incomplete_list for item in sublist][:-1]
    
    def format_as_state(self, command: str, new_state: str="end", next_place: str=None):
        return {
            command: {
                "state": new_state,
                "next_place": self.as_list(self.root + " " + next_place) if next_place else self.as_list(self.full_path + " " + new_state),
                "place_instance": next_place
                }
        }

    def alter_state(self, command: str):
        old_state =  self.states[self.state][command]
        self.state = self.complete_state + " " + self.states[self.state][command]["state"]
        return old_state
