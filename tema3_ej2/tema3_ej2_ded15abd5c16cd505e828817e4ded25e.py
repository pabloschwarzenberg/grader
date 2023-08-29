# crea la clase Vector y completa el código de la función suma_vectores usándola
import math

class Vector:
    def __init__(self,x,y,z):
        self.x=float(x)
        self.y=float(y)
        self.z=float(z)
        
    def norma(self):
        norma=math.sqrt(((self.x)**2) +((self.y)**2) +((self.z)**2))
        return norma
    
    def __add__(self,other):
        x3 = self.x + other.x
        y3 = self.y + other.y
        z3 = self.z + other.z
        return Vector(x3,y3,z3)
    
def suma_vectores(v1,v2):
    v3=v1+v2
    return v3
           