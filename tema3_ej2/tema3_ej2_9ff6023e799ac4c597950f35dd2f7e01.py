# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
  
  def norma(self):
    self.d=(self.x)**2
    self.f=(self.y)**2
    self.e=(self.z)**2
    return((self.d+self.f+self.e)**(1/2)) 
  
  def __add__(self,other):
    p=self.x+other.x
    q=self.y+other.y
    r=self.z+other.z
    return Vector(p,q,r)
    
def suma_vectores(v1,v2):
  v3 = v1 + v2
  return v3
           