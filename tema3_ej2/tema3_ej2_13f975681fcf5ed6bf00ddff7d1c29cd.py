# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector:
    def __init__(self,x,y,z):
      self.x=x
      self.y=y
      self.z=z
    def norma(self):
      norma=math.sqrt((self.x*self.x)+(self.y*self.y)+(self.z*self.z))
      return norma
    def __add__(self,other):
        suma_x=self.x+other.x
        suma_y=self.y+other.y
        suma_z=self.z+other.z
        r=Vector(suma_x,suma_y,suma_z)
        return r
def suma_vectores(v1,v2):
   return v1+v2
  
           