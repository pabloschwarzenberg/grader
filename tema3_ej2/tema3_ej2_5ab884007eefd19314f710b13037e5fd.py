class Vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
  def norma(self):
    norma=((self.x**2)+(self.y**2)+(self.z**2))**(1/2)
    return norma
  def __add__(self,other):
    vector=Vector(0,0,0)
    vector.x=self.x+other.x
    vector.y=self.y+other.y
    vector.z=self.z+other.z
    return vector
    
def suma_vectores(v1,v2):
  v3=v1+v2
  return v3