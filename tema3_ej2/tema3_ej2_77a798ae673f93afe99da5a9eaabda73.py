# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
    
  def norma(self):
    norma=(self.x**2+self.y**2+self.z**2)**(1/2)
    return norma
    
  def __add__(self,other):
    return suma_vectores(self,other)
    
def suma_vectores(self,other):
  if isinstance(self, Vector) and isinstance(other, Vector):
    x=self.x+other.x
    y=self.y+other.y
    z=self.z+other.z
    v=Vector(x,y,z)
    return v
    
  
           