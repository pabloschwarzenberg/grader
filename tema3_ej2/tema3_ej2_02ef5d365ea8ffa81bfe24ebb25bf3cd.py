import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        norma = math.sqrt(self.x**2+self.y**2+self.z**2)
        return norma

    def __str__(self):
        return str(self.x) + ' ' + str(self.y) + ' ' + str(self.z)

    def __add__(self, other):
        result = Vector(0, 0, 0)
        result.x = self.x + other.x
        result.y = self.y + other.y
        result.z = self.z + other.z
        return result


def suma_vectores(self, other):
    result = Vector(0, 0, 0)
    result.x = self.x + other.x
    result.y = self.y + other.y
    result.z = self.z + other.z
    return result