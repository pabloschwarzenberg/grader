# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        
    def norma(self):
        norma=math.sqrt((self.x)**2+(self.y)**2+(self.z)**2)
        return norma
        
    def __add__(self,other):
        v3= Vector(0,0,0)
        v3.x= self.x+other.x
        v3.y= self.y+other.y
        v3.z= self.z+other.z
        return v3
  
    def __str__(self):
        return [self.x,self.y,self.z]
     
def suma_vectores(v1,v2):
    if isinstance(v1,Vector)==True and isinstance(v2,Vector)==True:
        suma= v1+v2
        return suma
    else:
        return False