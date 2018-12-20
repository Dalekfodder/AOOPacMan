from character import Character


class PacMan(Character):
    __instance = None
    @staticmethod
    def get_pacman():
        if PacMan.__instance is None:
            PacMan()
        return PacMan.__instance

    def __init__(self):
        default_width = 303 - 16  # Width
        default_pacman_height = (7 * 60) + 19  # Pacman height
        if PacMan.__instance is not None:
            raise Exception("Singleton")
        else:
            PacMan.__instance = self
        super().__init__("images/pacman.png", default_width, default_pacman_height)
