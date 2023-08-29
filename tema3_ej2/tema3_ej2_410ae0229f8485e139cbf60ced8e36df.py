# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
    
  def norma(self):
    a=math.sqrt((self.x**2)+(self.y**2)+(self.z**2))
    return a
  def __add__(self,v2):
    x=self.x+v2.x
    y=self.y+v2.y
    z=self.z+v2.z
    return Vector(x,y,z)
def suma_vectores(v1,v2):
  v3 = v1+v2
  return v3
           