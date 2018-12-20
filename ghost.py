from character import Character
from ghost_strategy import *

from abc import ABC, abstractclassmethod

class Ghost(Character):
    def __init__(self, image, x, y, chase_behaviour, scatter_behaviour):
        super().__init__(image, x, y)

        self.chase_behaviour = chase_behaviour
        self.scatter_behaviour = scatter_behaviour
        self.frightened_behaviour = Frightened

    def perform_chase(self):
        self.chase_behaviour.chase()

    def perform_scatter(self):
        self.scatter_behaviour.scatter()

    def perform_frightened(self):
        self.frightened_behaviour.frightened()

class Blinky(Ghost):
    def __init__(self, image, x, y):
        super().__init__(image, x, y, ChaseAggresive, ScatterTopRight)

class Pinky(Ghost):
    def __init__(self, image, x, y):
        super().__init__(image, x, y, ChaseAmbush, ScatterTopLeft)

class Inky(Ghost):
    def __init__(self, image, x, y):
        super().__init__(image, x, y, ChasePatrol, ScatterBottomRight)

class Clyde(Ghost):
    def __init__(self, image, x, y):
        super().__init__(image, x, y, RandomChase, ScatterBottomLeft)



