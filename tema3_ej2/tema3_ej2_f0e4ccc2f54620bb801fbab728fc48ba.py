# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  def norma(self):
    modulo = (self.x**2 + self.y**2 + self.z**2)**(1/2)
    return modulo

  def __add__(self, other):
    new = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    return new

def suma_vectores(v1,v2):
  return v1 + v2
           