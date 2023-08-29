import math
class Vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
  def norma(self):
    norma=math.sqrt((self.x*2)+(self.y*2)+(self.z*2))
    return norma
  def __add__(self,other):
    xf= self.x + other.x
    yf= self.y + other.y
    zf= self.z + other.z
    vf=Vector(xf,yf,zf)
    return vf
 
  
def suma_vectores(v1,v2):
    vf = v1 + v2
    return vf
v1=Vector(1,1,1)
v2=Vector(1,1,1)
vf=suma_vectores(v1,v2)
print(vf)