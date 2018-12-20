from character import Character
from ghost_strategy import *
from abc import ABC, abstractclassmethod


class Ghost(Character):
    def __init__(self, image, x, y, chase_behaviour, scatter_behaviour, pac_man):
        super().__init__(image, x, y)

        self.chase_behaviour = chase_behaviour
        self.scatter_behaviour = scatter_behaviour
        self.frightened_behaviour = Frightened
        self.pac_man = pac_man


    def perform_chase(self):
        self.chase_behaviour.chase()

    def perform_scatter(self):
        self.scatter_behaviour.scatter()

    def perform_frightened(self):
        self.frightened_behaviour.frightened()


class Blinky(Ghost):
    def __init__(self, x, y, pac_man):
        super().__init__("images/Blinky.png", x, y, ChaseAggresive, ScatterTopRight, pac_man)


class Pinky(Ghost):
    def __init__(self, x, y, pac_man):
        super().__init__("images/Pinky.png", x, y, ChaseAmbush, ScatterTopLeft, pac_man)


class Inky(Ghost):
    def __init__(self, x, y, pac_man):
        super().__init__("images/Inky.png", x, y, ChasePatrol, ScatterBottomRight, pac_man)


class Clyde(Ghost):
    def __init__(self, x, y, pac_man):
        super().__init__("images/Clyde.png", x, y, RandomChase, ScatterBottomLeft, pac_man)
