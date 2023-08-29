# crea la clase Vector y completa el código de la función suma_vectores usándola
from math import *
class Vector:
  def __init__(self, argx, argy, argz):
    self.x = argx
    self.y = argy
    self.z = argz
  def norma(self):
    norma = sqrt((pow(self.x,2))+(pow(self.y,2))+(pow(self.z,2)))
    return norma
  def __add__(self,other):
    x = (self.x + other.x)
    y = (self.y + other.y)
    z = (self.z + other.x)
    ans = Vector(x,y,z)
    return ans

def suma_vectores(v1,v2):
  v3 = v1+v2  
  return v3
           