from character import Character
from ghost_strategy import *
from pac_man import PacMan


class Ghost(Character):
    def __init__(self, image, x, y, chase_behaviour, scatter_behaviour):
        super().__init__(image, x, y)

        self.chase_behaviour = chase_behaviour
        self.scatter_behaviour = scatter_behaviour
        self.frightened_behaviour = Frightened
        self.pac_man = PacMan.get_pacman()


    def perform_chase(self):
        self.chase_behaviour.chase()

    def perform_scatter(self):
        self.scatter_behaviour.scatter()

    def perform_frightened(self):
        self.frightened_behaviour.frightened()


class ConcreteBlinky(Ghost):
    def __init__(self, x, y):
        super().__init__("images/Blinky.png", x, y, ChaseAggresive, ScatterTopRight)


class ConcretePinky(Ghost):
    def __init__(self, x, y):
        super().__init__("images/Pinky.png", x, y, ChaseAmbush, ScatterTopLeft)


class ConcreteInky(Ghost):
    def __init__(self, x, y):
        super().__init__("images/Inky.png", x, y, ChasePatrol, ScatterBottomRight)


class ConcreteClyde(Ghost):
    def __init__(self, x, y):
        super().__init__("images/Clyde.png", x, y, RandomChase, ScatterBottomLeft)
