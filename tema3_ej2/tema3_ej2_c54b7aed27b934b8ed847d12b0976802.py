# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        norm = math.sqrt((self.x ** 2) + (self.y ** 2) + (self.z ** 2))
        return norm

    def __add__(self, other):
        x=self.x+other.x
        y = self.y + other.y
        z = self.z + other.z
        v=Vector(x,y,z)
        return v
        

def suma_vectores(v1, v2):
    v3 = Vector(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z)
    return v3
