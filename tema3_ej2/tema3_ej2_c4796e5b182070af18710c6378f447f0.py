#Clase Vector3D
class Vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
  
  def norma (self):
    d=(self.x)**2
    f=(self.y)**2
    e=(self.z)**2
    return((d+f+e)**(1/2))
  
  def __add__(self,other):
    p=self.x+other.x
    q=self.y+other.y
    r=self.z+other.z
    return Vector(p,q,r)
    
def suma_vectores(v1,v2):
  c1=v1.x+v2.x
  c2=v1.y+v2.y
  c3=v1.z+v2.z
  return Vector(c1,c2,c3)         