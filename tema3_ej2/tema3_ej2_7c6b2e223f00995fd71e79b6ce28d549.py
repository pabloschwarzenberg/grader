# crea la clase Vector y completa el código de la función suma_vectores usándola
def suma_vectores(v1,v2):
  return Vector(v1.x+v2.x,v1.y+v2.y,v1.z+v2.z)

class Vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
  def __add__ (self,vector_b):
    return Vector(self.x+vector_b.x,self.y+vector_b.y,self.z+vector_b.z)
  
  def norma(self):
    return (self.x**2+self.y**2+self.z**2)**(1/2)
           