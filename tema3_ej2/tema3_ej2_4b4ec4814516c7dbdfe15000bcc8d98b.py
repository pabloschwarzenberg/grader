
# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def norma(self):
        self.norma=math.sqrt(self.x**2+self.y**2+self.z**2)
        return self.norma
    def __add__(self,other):
        self.suma=((self.x+other.x),(self.y+other.y),(self.z+other.z))
        return self.suma
        
 def suma_vectores(v1,v2):
    v1=Vector(1,2,3)
    v2=Vector(2,3,4)
    v3=v1+v2
    return v3