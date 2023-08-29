# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
  def norma(self):
    norma_x=self.x**2
    norma_y=self.y**2
    norma_z=self.z**2
    norma_total=math.sqrt(norma_x+norma_y+norma_z)
    return norma_total
  def __add__(self,other):
    suma_x=self.x+other.x
    suma_y=self.y+other.y
    suma_z=self.z+other.z

    r=Vector(suma_x,suma_y,suma_z)
    return r
def suma_vectores(v1,v2):
  return v1+v2
           