from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self):
        self.speed = 0

    @abstractmethod
    def can_move(self):
        raise NotImplementedError("Missing can_move Implementation.")

    @abstractmethod
    def move(self, direction):
        raise NotImplementedError("Missing move Implementation.")

