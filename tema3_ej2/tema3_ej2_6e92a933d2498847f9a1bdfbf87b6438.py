# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector:
  def __init__(self,x0=0,y0=0,z0=0):
    self.x=x0
    self.y=y0
    self.z=z0
  def norma(self):
    return math.sqrt(self.x**2+self.y**2+self.z**2)
  def __add__(self,otro):
   return Vector(self.x+otro.x,self.y+otro.y,self.z+otro.z)
def suma_vectores(v1,v2):
    return Vector(v1.x+v2.x,v1.y+v2.y,v1.z+v2.z)