class ChaseBehaviour:
    def chase(self):
        raise NotImplementedError("Missing Chase Implementation.")


class ScatterBehaviour:
    def scatter(self):
        raise NotImplementedError("Missing Scatter Implementation.")


class FrigtenedBehaviour:
    def frightened(self):
        raise NotImplementedError("Missing Frightened Implementation.")


class ChaseAggresive(ChaseBehaviour):
    def chase(self):
        pass


class ChasePatrol(ChaseBehaviour):
    def chase(self):
        pass


class ChaseAmbush(ChaseBehaviour):
    def chase(self):
        pass


class RandomChase(ChaseBehaviour):
    def chase(self):
        pass


class ScatterBottomLeft(ScatterBehaviour):
    def scatter(self):
        pass


class ScatterBottomRight(ScatterBehaviour):
    def scatter(self):
        pass


class ScatterTopLeft(ScatterBehaviour):
    def scatter(self):
        pass


class ScatterTopRight(ScatterBehaviour):
    def scatter(self):
        pass


class Frightened(FrigtenedBehaviour):
    def frightened(self):
        pass
