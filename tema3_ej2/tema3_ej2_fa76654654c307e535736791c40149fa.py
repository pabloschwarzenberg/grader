# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
def suma_vectores(v1,v2):
    x = v1.x + v2.x
    y = v1.y + v2.y
    z = v1.z + v2.z
    v3=Vector(x,y,z)
    return v3
    
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def norma(self):
        d = math.sqrt(self.x**2 + self.y**2 + self.x**2)
        return d
        
    def __add__(self, other):
        v3 = suma_vectores(self, other)
        return v3