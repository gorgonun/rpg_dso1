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
        return self.complete_state

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
    def top(self):
        return self.map_state(self.full_path)[-1]

    def map_state(self, states: list):
        incomplete_list = list(map(lambda x: [x, "places"], states))
        return [item for sublist in incomplete_list for item in sublist][:-1]
    
    def format_as_state(self, command: str, new_state: list=[], next_place: str=None):
        return {
            command: {
                "state": new_state,
                "next_place": self.map_state([next_place]) if next_place else self.map_state(self.full_path + new_state),
                "place_instance": next_place
                }
        }

    def alter_state(self, command: str):
        old_state = self.states[self.state][command]
        self.state = self.complete_state + self.states[self.state][command]["state"]
        return old_state
