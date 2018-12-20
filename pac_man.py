from character import Character


class PacMan(Character):
    __instance = None

    @staticmethod
    def get_pacman():
        if PacMan.__instance is None:
            PacMan()
        return PacMan.__instance

    def __init__(self, image, x, y):
        if PacMan.__instance != None:
            self.change_x = x
            self.change_y = y
        else:
            PacMan.__instance = self
        super().__init__(image, x, y)