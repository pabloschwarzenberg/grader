import math
class Vector:
 def __init__(self,x,y,z):
  self.x = x
  self.y = y
  self.z = z
 def norma(self):
   norma = math.sqrt(self.x**2+self.y**2+self.z**2)
   return norma
 def __add__(self,other):
     return Vector(self.x + other.x , self.y + other.y , self.z + other.z)
 def __str__(self):
      return str(self.x)+","+str(self.y)+","+str(self.z)


def suma_vectores(v1,v2):
    return v1 + v2





