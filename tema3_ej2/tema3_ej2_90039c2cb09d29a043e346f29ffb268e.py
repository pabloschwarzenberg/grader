# crea la clase Vector y completa el código de la función suma_vectores usándola
from math import sqrt
class Vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
    
    
  def norma(self):
    norma=sqrt(((self.x)*(self.x)+(self.y)*(self.y)+(self.z)*(self.z)))
    return norma
    
  def __add__(self, v2):
    return suma_vectores(self, v2)
    
def suma_vectores(v1,v2):
  x_s=v1.x+v2.x
  y_s=v1.y+v2.y
  z_s=v1.z+v2.z
  vs=Vector(x_s,y_s,z_s)
  return vs
           