# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector():
  def __init__(self,x,y,z):
    self.x = x
    self.y = y
    self.z = z
    
  def norma(self):
    return int(((self.x)**2+(self.y)**2+(self.z)**2)**2)
  def __add__(v1, v2):
    x = v1.x + v2.x
    y = v1.y + v2.y
    z = v1.z + v2.z
    return Vector(x,y,z)

def suma_vectores(v1,v2):
  x = v1.x + v2.x
  y = v1.y + v2.y
  z = v1.z + v2.z
  return Vector(x,y,z)
           