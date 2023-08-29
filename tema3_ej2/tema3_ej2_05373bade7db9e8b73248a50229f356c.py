# crea la clase Vector y completa el código de la función suma_vectores usándola
from math import sqrt
class Vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
    
  def norma(self):
    norma=sqrt((self.x)*(self.x)+(self.y)*(self.y)+(self.z)*(self.z))
    return norma
   
  def __add__(self, v2):
    return suma_vectores(self, v2)
    
def suma_vectores(v1,v2):
    suma_x=int(v1.x)+int(v2.x)
    suma_y=int(v1.y)+int(v2.y)
    suma_z=int(v1.z)+int(v2.z)
    return Vector(suma_x,suma_y,suma_z)
           