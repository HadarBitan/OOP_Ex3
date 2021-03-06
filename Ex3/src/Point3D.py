import math


class Point3D:

    def __init__(self, x: float, y: float, z: float):
        self._x = x
        self._y = y
        self._z = z

    def get_x(self) -> float:
        return self._x

    def get_y(self) -> float:
        return self._y

    def get_z(self) -> float:
        return self._z

    def distance(self, other) -> float:
        dx = self._x - other.get_x()
        dy = self._y - other.get_y()
        dz = self._z - other.get_z()
        return math.sqrt(math.pow(dx, 2) + math.pow(dy, 2) + math.pow(dz, 2))