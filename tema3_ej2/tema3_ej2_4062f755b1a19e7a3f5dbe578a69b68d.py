# crea la clase Vector y completa el código de la función suma_vectores usándola
def suma_vectores(v1,v2):
  c = v1 + v2
  return c


class Vector:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
    
  def norma(self):
    n = (self.x**2 + self.y**2 + self.z**2)**(1/2)
    return n
    
  def __add__(self, other):
    a = self.x + other.x
    b = self.y + other.y
    c = self.z + other.z
    return (a, b, c)
    
  def __str__(self):
    print(self.__add__())