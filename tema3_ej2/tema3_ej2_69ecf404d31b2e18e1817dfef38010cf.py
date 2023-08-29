# crea la clase Vector y completa el código de la función suma_vectores usándola
import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "{0},{1},{2}".format(float(self.x),float(self.y),float(self.z))

    def norma(self):
        return (float(self.x) ** 2 + float(self.y) ** 2 + float(self.z) ** 2)**1/2

    def __add__(self,other):
        self.x = self.x + other.x
        self.y = self.y + other.y
        self.z = self.z + other.z
           
def suma_vectores(v1, v2):
  a = v1 + v2
  return a