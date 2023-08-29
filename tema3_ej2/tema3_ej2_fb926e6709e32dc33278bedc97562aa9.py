# crea la clase Vector y completa el código de la función suma_vectores usándola
from math import sqrt
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def norma(self):
        return sqrt((self.x)**2+(self.y)**2+(self.z)**2)
    def __add__(self,other):
        return suma_vectores(self,other)
def suma_vectores(v1,v2):
    x=v1.x+v2.x
    y=v1.y+v2.y
    z=v1.z+v2.z
    v3=Vector(x,y,z)
    return v3
           