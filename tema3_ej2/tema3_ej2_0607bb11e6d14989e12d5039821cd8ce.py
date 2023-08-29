class Vector:
  def __init__(self,X,Y,Z):
    self.x=X
    self.y=Y
    self.z=Z
  def norma(self):
    Norma=(self.x**2+self.y**2+self.z**2)**(1/2)
    return Norma
  def __add__(self,other):
    VectorSuma=Vector(self.x+other.x,self.y+other.y,self.z+other.z)
    return VectorSuma
def suma_vectores(a,b):
 Resultado=a+b
 return Resultado