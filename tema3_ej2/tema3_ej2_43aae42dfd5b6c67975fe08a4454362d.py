class Vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
  def norma(self):
    n=((self.x**2)+(self.y**2)+(self.z**2))**(1/2)
    return n
  def __add__(self,other):
    v3=Vector(self.x+other.x,self.y+other.y,self.z+other.z)
    return v3
def suma_vectores(v1,v2):
  x=v1.__add__(v2)
  return x
           