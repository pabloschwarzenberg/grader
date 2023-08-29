# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
  def __init__(self,x=0,y=0,z=0):
    self.x=x
    self.y=y
    self.z=z
  def norma(self):
    norma=self.x*self.x+self.y*self.y+self.z*self.z
    norma=norma**(1/2)
    return norma
  def __add__(self,otro):
    return suma_vectores(self,otro)
def suma_vectores(v1,v2):
  v3=Vector(v1.x+v2.x,v1.y+v2.y,v1.z+v2.z)
  return v3
           