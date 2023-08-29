# crea la clase Vector y completa el código de la función suma_vectores usándola
import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def norma(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def __add__(self, otro_vector):
        nuevo_x = self.x + otro_vector.x
        nuevo_y = self.y + otro_vector.y
        nuevo_z = self.z + otro_vector.z
        return Vector(nuevo_x, nuevo_y, nuevo_z)


def suma_vectores(vector1, vector2):
    nuevo_x = vector1.x + vector2.x
    nuevo_y = vector1.y + vector2.y
    nuevo_z = vector1.z + vector2.z
    return Vector(nuevo_x, nuevo_y, nuevo_z)
