# crea la clase Vector y completa el código de la función suma_vectores usándola
import math 
class Vector:
   def __init__(self,x,y,z):
       self.x=x
       self.y=y
       self.z=z
       
   def norma(self):
        r= math.sqrt(self.x**2 + self.y**2 + self.z**2)
        return r 
        
   def __add__(self,other):
        r=Vector(0,0,0)
        x3=(self.x + other.x)
        y3=(self.y + other.y)
        z3=(self.z + other.z)
        r=Vector(x3,y3,z3)
        return r
    
def suma_vectores(v1,v2):
    return v1 + v2
           