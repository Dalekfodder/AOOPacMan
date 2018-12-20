from character import Character
from ghost_strategy import *

from abc import ABC, abstractclassmethod

class Ghost(Character):
    def __init__(self, image, x, y, chase_behaviour, scatter_behaviour):
        super().__init__(image, x, y)

        self.chase_behaviour = chase_behaviour
        self.scatter_behaviour = scatter_behaviour
        self.frightened_behaviour = Frightened
