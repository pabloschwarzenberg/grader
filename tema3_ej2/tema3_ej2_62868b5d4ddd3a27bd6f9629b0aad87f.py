# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector:
  def __init__(self,x,y,z):
    self.x=float(x)
    self.y=float(y)
    self.z=float(z)
  def norma(self):
    n=self.x**2 + self.y**2 + self.z**2
    resultado= n**0.5
    return resultado
  def __add__(self,other):
    self.x+=other.x
    self.y+=other.y
    self.z+=other.z
    return self
def suma_vectores(v1,v2):
  vn=Vector(v1.x+v2.x,v1.y+v2.y,v1.z+v2.z)
  return vn