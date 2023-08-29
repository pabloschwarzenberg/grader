# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def norma(self):
        norma = math.sqrt((self.x)**2+(self.y)**2+(self.z)**2)
        return norma
    def __add__(self, other):
        v1 = Vector(self.x+other.x,self.y+other.y,self.z+other.z)
        return v1

def suma_vectores(v1,v2):
    v1 = Vector(v1.x+v2.x,v1.y+v2.y,v1.z+v2.z)
    return v1