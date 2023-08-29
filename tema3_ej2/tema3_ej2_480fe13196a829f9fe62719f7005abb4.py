# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector3d:
  def __init__(self,x,y,z):
      self.x=x
      self.y=y
      self.z=z
    
  def norma(self):
    a=int(self.x)
    b=int(self.y)
    d=int(self.z)
    c=math.sqrt(a*a+b*b+c*c)
    return c
  def modulo(self):
    a=int(self.x)
    b=int(self.y)
    d=int(self.z)
    c=math.sqrt(a*a+b*b+c*c)
    return c
  def __add__(self,other):
    r=Vector3d(x,y,z)
    r.x=self.x+other.x
    r.y=self.y+other.y
    r.z=self.z+other.z
    return r
  def suma_vectores(self,other):
    r=Vector3d(x,y,z)
    r.x=self.x+other.x
    r.y=self.y+other.y
    r.z=self.z+other.z
    return r
           