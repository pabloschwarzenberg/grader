# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def suma_vectores(self,other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    def norma(self):
        return (math.sqrt(self.x**2 + self.y**2 + self.z**2))
    def __add__(self,other):
      if type(self) == Vector and type(other) == Vector:
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)