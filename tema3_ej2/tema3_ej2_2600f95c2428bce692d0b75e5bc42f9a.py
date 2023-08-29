# crea la clase Vector y completa el código de la función suma_vectores usándola
import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __add__(self, otro):
        suma_x = self.x + otro.x
        suma_y = self.y + otro.y
        suma_z = self.z + otro.z
        return Vector(suma_x, suma_y, suma_z)

def suma_vectores(v1, v2):
    suma_x = v1.x + v2.x
    suma_y = v1.y + v2.y
    suma_z = v1.z + v2.z
    return Vector(suma_x, suma_y, suma_z)
  