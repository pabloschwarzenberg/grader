# crea la clase Vector y completa el código de la función suma_vectores usándola
from math import sqrt
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def norma(self):
        norma=sqrt((self.x)**2+(self.y)**2+(self.z)**2)
        return norma
    def __add__(self,v2):  
        return suma_vectores(self,v2)
def suma_vectores(v1,v2):
    suma=Vector(v1.x+v2.x,v1.y+v2.y,v1.z+v2.z)
    return suma
        
        
