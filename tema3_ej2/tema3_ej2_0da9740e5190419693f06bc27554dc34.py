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

def suma_vectores(vec1,vec2):
    x=vec1.x+vec2.x
    y=vec1.y+vec2.y
    z=vec1.z+vec2.z
    vv=Vector(x,y,z)
    return vv
    

    