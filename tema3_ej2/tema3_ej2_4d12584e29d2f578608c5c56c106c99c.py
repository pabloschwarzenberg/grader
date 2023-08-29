import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

def suma_vectores(v1, v2):
    return Vector(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z)

    def __add__(self, otro_vector):
        x_nuevo = self.x + otro_vector.x
        y_nuevo = self.y + otro_vector.y
        z_nuevo = self.z + otro_vector.z
        return Vector(x_nuevo, y_nuevo, z_nuevo)