# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
  def norma(self):
    norm=(self.x**2+self.y**2+self.z**2)**0.5
    return norm
  def __add__(self,otro):
    return suma_vectores(self, otro)
   
def suma_vectores(v1,v2):
  x=v1.x+v2.x
  y=v1.y+v2.y
  z=v1.z+v2.z
  return Vector(x,y,z)
  
  
  return
           