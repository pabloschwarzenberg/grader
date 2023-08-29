import math
class Vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
  
  def norma(self):
    norma=math.sqrt(math.pow(self.x,2)+math.pow(self.y,2)+math.pow(self.z,2))
    return norma
  
  def __add__(self,v1):
    v2=Vector(0,0,0)
    v2.x=self.x+v1.x
    v2.y=self.y+v1.y
    v2.z=self.z+v1.z
    return v2
    
  def suma_vectores(self,v1):
    v2=self+v1
    return v2