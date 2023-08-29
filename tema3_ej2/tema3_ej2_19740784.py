# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
  def norma(self):
    norma=self.x**2 + self.y**2 + self.z**2
    norma=norma**(1/2)
    return norma
  def __add__(v1,v2):
     addx=v1.x+v2.x
     addy=v1.y+v2.y
     addz=v1.z+v2.z
     vectornuevo=Vector(addx,addy,addz)
     return vectornuevo
def suma_vectores(v1,v2):
    def __add__(v1,v2):
      addx=v1.x+v2.x
      addy=v1.y+v2.y
      addz=v1.z+v2.z
      vectornuevo=Vector(addx,addy,addz)
      return vectornuevo
           