# crea la clase Vector y completa el código de la función suma_vectores usándola
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
    r = Vector(0,0,0)
    r = self.x + other.x
    r = self.y + other.y
    r = self.z + other.z
    return r
  def suma_vectores(self,v1,v2):
    r = Vector(0,0,0)
    r = v1.x + v2.x
    r = v1.y + v2.y
    r = v1.z + v2.z
    return r
           