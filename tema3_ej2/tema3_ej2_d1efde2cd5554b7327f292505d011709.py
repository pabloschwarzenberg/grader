# crea la clase Vector y completa el código de la función suma_vectores usándola
from math import sqrt
class Vector:
  def __init__(self,x,y,z):
    self.x = x
    self.y = y
    self.z = z
  def norma(self):
    parteX = (self.x)**2
    parteY = (self.y)**2
    parteZ = (self.z)**2
    normaN = sqrt(parteX+parteY+parteZ)
    return normaN
  def __add__(self, other):
    v3x = self.x + other.x 
    v3y = self.y + other.y
    v3z = self.z + other.z
    v3 = Vector(v3x,v3y,v3z)
    return v3
def suma_vectores(v1,v2):
  return v1+v2

  
  return
           