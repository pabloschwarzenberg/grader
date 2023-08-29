# crea la clase Vector y completa el código de la función suma_vectores usándola
from math import sqrt
class Vector:
     def __init__(self,x,y,z):
         self.x = x
         self.y = y
         self.z = z
     
     def __add__(self,other):
         cx = self.x + other.x
         cy = self.y + other.y
         cz = self.z + other.z
         c = Vector(cx,cy,cz)
         return c
     
           
     
     def norma(self):
         x = self.x ** 2
         y = self.y ** 2
         z = self.z ** 2
         n = sqrt(x+y+z)
         return n
     
def suma_vectores(v1,v2):
     v3 = v1 + v2
     return v3 
 
              
        



     
 
 
              
           