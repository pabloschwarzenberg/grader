# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
    
  def __add__(self,other):
      a = self.x + other.x
      b = self.y + other.y
      c = self.z + other.z
      return Vector(a, b, c)
  
  def norma(self):
    n = ((self.x**2)+(self.y**2)+(self.z**2))**(1/2)
    return n
    
def suma_vectores(v1,v2):
  suma = v1 + v2
  return suma
           