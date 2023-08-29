# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def norma(self):
        norma=math.sqrt(self.x**2+self.y**2+self.z**2)
        return norma
    def __add__(self,other):
        a=self.x+other.x
        b=self.y+other.y
        c=self.z+other.z
        return Vector(a,b,c)
        
    
    def __str__(self):       
        return ("("+str(self.x)+","+str(self.y)+","+str(self.z)+")")

def suma_vectores(v1,v2):
    a=v1.x+v2.x
    b=v1.y+v2.y
    c=v1.z+v2.z
    return Vector(a,b,c)

v1=Vector(1,2,3)
v2=Vector(8,7,6)

print(v1.norma())
print(suma_vectores(v1,v2))
print(v1+v2)

