import math
class Vector:
  def __init__(self,x,y,z):
    self.x=float(x)
    self.y=float(y)
    self.z=float(z)
  def norma(self):
    norma=math.sqrt((self.x**2)+(self.y**2)+(self.z**2))
    self.modulo=norma
    return norma
  def suma_vectores(self,other):
    r=Vector(0,0,0)
    r.x=self.x+other.x
    r.y=self.y+other.y
    r.z=self.z+other.z
    return r
  def __add__(self,other):
    r=Vector(0,0,0)
    r.x=self.x+other.x
    r.y=self.y+other.y
    r.z=self.z+other.z
    return r