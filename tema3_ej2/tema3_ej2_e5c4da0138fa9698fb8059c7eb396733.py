# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
  def __init__(self,x,y,z):
    self.x = x
    self.y = y
    self.z = z
  def norma(self):
    return (self.x**2+self.y**2+self.z**2)**0.5
  def __add__(self, v2):
    return suma_vectores(self,v2)
  
def suma_vectores(v1,v2):
  sx = v1.x + v2.x
  sy = v1.y + v2.y
  sz = v1.z + v2.z
  return Vector(sx,sy,sz)
           