# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
  def __init__(self, x, y, z):
    self.x=float(x)
    self.y=float(y)
    self.z=float(z)
  
  def norma(self):
    return int(((self.x**2)+(self.y**2)+(self.z**2))**(1/2))
  def __add__(self,other):
    x=int(self.x) + int(other.x)
    y=int(self.y) + int(other.y)
    z=int(self.z) + int(other.z)
    return Vector(x, y, z)
    
def suma_vectores(self,other):
    x=int(self.x) + int(other.x)
    y=int(self.y) + int(other.y)
    z=int(self.z) + int(other.z)
    return Vector(x, y, z)