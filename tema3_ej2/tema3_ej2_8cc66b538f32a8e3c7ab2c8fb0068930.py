# crea la clase Vector y completa el código de la función suma_vectores usándola
import math

class Vector:
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z
    def norma(self, norma):
        norma=math.sqrt((self.x * self.x) + (self.y * self.y) + (self.z * self.z))
        return norma
    

def suma_vectores(v1,v2):
    x3 = v1.x + v2.x
    y3 = v1.y + v2.y
    z3 = v1.z + v2.z
    v3 = Vector(x3, y3, z3)
    return v3