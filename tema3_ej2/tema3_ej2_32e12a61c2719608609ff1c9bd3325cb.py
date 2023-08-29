class Vector:

  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
  def __str__(self):
    return "({0},{1},{2})".format(self.x,self.y,self.z)

  def __add__(self, otro):
    return Vector(self.x+otro.x,self.y+otro.y,self.z+otro.z)
  def norma(self):
    return int((self.x**2 + self.y**2 + self.z**2)**(1/2))
  def suma_vectores(self,otro):
    return Vector(self+otro)




           