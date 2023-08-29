# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector:
    def __init__(self,x,y,z):
        self.x=float(x)
        self.y=float(y)
        self.z=float(z)
    def norma(self):
        largovector=float(math.sqrt(self.x**2+self.y**2+self.z**2))
        return largovector
        
    def __add__(self,other):
        suma=suma_vectores(self,other)
        return suma
    def __str__(self):
        return "({},{},{})".format(self.coordx,self.coordy,self.coordz)
def suma_vectores(v1,v2):
    r=Vector(0,0,0)
    r.x=v1.x+v2.x
    r.y=v1.y+v2.y
    r.z=v1.z+v2.z
    return r
    

           