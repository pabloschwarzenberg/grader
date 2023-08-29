# crea la clase Vector y completa el código de la función suma_vectores usándola
import math

def suma_vectores(v1,v2):
  x=v1.x+v2.x
  y=v1.y+v2.y
  z=v1.z+v2.z
  return Vector(x,y,z)

class Vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
  def norma(self):
    sum_quad=self.x**2+self.y**2+self.z**2
    return math.sqrt(sum_quad)
  def __add__(self,other):
    if isinstance(self,Vector) and isinstance(other,Vector):
      return suma_vectores(self,other)
    else:
      raise TypeError("Ambos objetos deben ser de la clase vector")