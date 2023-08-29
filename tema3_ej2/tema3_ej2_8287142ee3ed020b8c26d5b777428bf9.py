import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __add__(self, otro_vector):
        suma_x = self.x + otro_vector.x
        suma_y = self.y + otro_vector.y
        suma_z = self.z + otro_vector.z
        return Vector(suma_x, suma_y, suma_z)

def suma_vectores(v1, v2):
    return v1 + v2

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

v3 = suma_vectores(v1, v2)
print(v3.x, v3.y, v3.z)

norma_v3 = v3.norma()
print(norma_v3)
