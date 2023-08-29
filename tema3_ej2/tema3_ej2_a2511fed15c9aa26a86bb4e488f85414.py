# crea la clase Vector y completa el código de la función suma_vectores usándola
import math


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        x = self.x
        y = self.y
        z = self.z
        norma = abs(math.sqrt(x ** 2 + y ** 2 + z ** 2))
        return norma

    def __add__(v1, v2):
        v1x = v1.x
        v1y = v1.y
        v1z = v1.z
        v2x = v2.x
        v2y = v2.y
        v2z = v2.z
        v3x = v1x + v2x
        v3y = v1y + v2y
        v3z = v1z + v2z
        v3 = Vector(v3x, v3y, v3z)
        return v3


def suma_vectores(v1, v2):
    v1x = v1.x
    v1y = v1.y
    v1z = v1.z
    v2x = v2.x
    v2y = v2.y
    v2z = v2.z
    v3x = v1x + v2x
    v3y = v1y + v2y
    v3z = v1z + v2z
    v3 = Vector(v3x, v3y, v3z)
    return v3
