# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
  def __str__(self):
    return "{0},{1},{2}".format(self.x,self.y,self.z)
  def norma(self):
    return ((self.x)**2+(self.y)**2+(self.z)**2)**(1/2)
  def suma_vectores(self,other):
    self.x=self.x+other.x
    self.y=self.y+other.y
    return Vector
   