# crea la clase Vector y completa el código de la función suma_vectores usándola
import math as m
def suma_vectores(v1,v2):
  new_vector = Vector(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z)
  return new_vector
class Vector:
      def __init__(self, x, y, z):
          self.x = float(x)
          self.y = float(y)
          self.z = float(z)
      
      def norma(self):
          d = m.sqrt(self.x**2 + self.y**2 + self.x**2)
          return d
      
      def __add__(self, other):
          new_vector = suma_vectores(self, other)
          return new_vector
