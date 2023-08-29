# crea la clase Vector y completa el código de la función suma_vectores usándola
import math

def suma_vectores(v1,v2):
    return v1+v2
class Vector:

    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def norma(self):
        n=math.sqrt(self.x**2+self.y**2+self.z**2)
        return n

    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        z=self.z+other.z
        return Vector(x,y,z)

    def __str__(self):
        return "{0},{1},{2}".format(self.x,self.y,self.z)
           