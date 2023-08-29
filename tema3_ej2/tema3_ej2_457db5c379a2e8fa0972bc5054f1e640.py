import math
class vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
    
  def suma_vectores(v1,v2):
    x3=v1.x+v2.x
    y3=v1.y+v2.y
    z3=v1.z+v2.z
    v3=vector(x3,y3,z3)
    return v3
    
  def norma(self):
    norma=math.sqrt((x**2)+(y**2)+(z**3))
    return norma
    
           