# crea la clase Vector y completa el código de la función suma_vectores usándola
from math import*
class Vector:    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return "( " + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + " )'"
    def __add__(self, v):
        sumax = self.x + v.x
        sumay = self.y + v.y
        sumaz = self.z + v.z
        suma = Vector(sumax, sumay, sumaz)
        return suma
    def norma(self):
        norma = sqrt(self.x*self.x + self.y*self.y + self.z*self.z)
        if norma==1:
            return int(norma)
        else:
            return norma        
def suma_vectores(v1,v2):
    suma_vectores = Vector(v1.x+v2.x, v1.y+v2.y, v1.z+v2.z)
    return suma_vectores             
            
            
