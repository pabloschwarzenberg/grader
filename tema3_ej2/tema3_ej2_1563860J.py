# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector:

    def __init__ (self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def norma(self):
        norma=math.sqrt(self.x**2+self.y**2+self.z**2)
        return norma
    def __add__(self,other):
        v=Vector(0,0,0)
        v.x=self.x+other.x
        v.y=self.y+other.y
        v.z=self.z+other.z
        return v
        
v1=Vector(3,4,5)
v2=Vector(3,4,5)
def suma_vectores(v1,v2):
    return Vector(v1.x+v2.x,v1.y+v2.y,v1.z+v2.z)
        
  
           