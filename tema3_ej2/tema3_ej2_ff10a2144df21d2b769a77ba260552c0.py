# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def norma(self):
        norma=math.sqrt((self.x**2)+(self.y**2)+(self.z**2))
        return norma
        
    def __add__(self,other):
        r=Vector(0,0,0)
        r.x=self.x+other.x
        r.y=self.y+other.y
        r.z=self.z+other.z
        return r
        
def suma_vectores(v1,v2):
    return v1.__add__(v2)

v1=Vector(1,2,3)
v2=Vector(4,5,6)
v3=suma_vectores(v1,v2)
print(v3)