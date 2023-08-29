# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
  def norma(self):
    return math.sqrt(self.x**2+self.y**2+self.z**2)
  def __add__(self,other):
    xs=self.x + other.x
    ys=self.y + other.y
    zs=self.z + other.z
    return Vector(xs,ys,zs)
  
def suma_vectores(v1,v2):
  x=v1.x+v2.x  
  y=v1.y+v2.y
  z=v1.z+v2.z
  vv=Vector(x,y,z)
  return vv