class Vector:
  def __init__(self,x1,x2,x3):
    self.x=x1
    self.y=x2
    self.z=x3

  def __str__(self):
    return {self.x}, {self.y},{self.y}
  def __add__(self, otro):
    return (self.x+otro.x , self.y+otro.y,self.z+otro.z)

  def norma(self):
    return(((self.x)**(2)+(self.y)**(2)+(self.z)**(2))**(0.5))

def suma_vectores(v1,v2):
  def __str__(self):
    return {self.x}, {self.y},{self.y}
  def __add__(self, otro):
    return (self.x+otro.x , self.y+otro.y,self.z+otro.z)
  print(v1+v2)

a=Vector(1,4,3)
b=Vector(3,4,3)
suma_vectores(Vector(1,4,3),Vector(3,4,3))
