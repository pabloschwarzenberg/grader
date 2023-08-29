# crea la clase Vector y completa el código de la función suma_vectores usándola

import math
class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def norma(self):
       Norma = math.sqrt(self.x**2+self.y**2+self.z**2)
       return Norma
    def __str__(self):
       return "("+str(self.x)+","+str(self.y)+","+str(self.z)+")"

    def __add__(self,other):
        wx = self.x + other.x
        wy = self.y + other.y
        wz = self.z + other.z
        return Vector(wx,wy,wz)

def suma_vectores(v1,v2):
  wx = v1.x + v2.x
  wy = v1.y + v2.y
  wz = v1.z + v2.z
  suma_vectores = Vector(wx,wy,wz)
  return suma_vectores


           