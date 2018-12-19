from character import Character
from ghost_strategy import *

from abc import ABC, abstractclassmethod

class Ghost(Character):
    def __init__(self, chase_behaviour, scatter_behaviour, frightened_behaviour):
        self.chase_behaviour = chase_behaviour
        self.scatter_behaviour = scatter_behaviour
        self.frightened_behaviour = frightened_behaviour