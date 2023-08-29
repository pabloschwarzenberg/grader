# crea la clase Vector y completa el código de la función suma_vectores usándola
import math


def suma_vectores(v1, v2):
    return Vector(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z)


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __add__(self, other):
        return suma_vectores(self, other)
