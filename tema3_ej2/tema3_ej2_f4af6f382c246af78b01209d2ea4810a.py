# crea la clase Vector y completa el código de la función suma_vectores usándola
import math

def suma_vectores(v1,v2):
  sum = Vector(v1.x+v2.x, v1.y+v2.y, v1.z+v2.z)  
  return sum

class Vector:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
  
  def norma(self):
    norma = math.sqrt((self.x)**2+(self.y)**2+(self.z)**2)
    return norma
    