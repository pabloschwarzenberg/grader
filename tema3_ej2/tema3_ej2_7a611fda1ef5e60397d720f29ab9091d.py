import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

def suma_vectores(vector1, vector2):
    x = vector1.x + vector2.x
    y = vector1.y + vector2.y
    z = vector1.z + vector2.z
    return Vector(x, y, z)
