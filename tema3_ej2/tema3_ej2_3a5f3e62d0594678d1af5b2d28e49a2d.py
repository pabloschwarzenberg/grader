# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
  def norma(self):
    norma=(self.x)**2+(self.y)**2+(self.z)**2
    norma=(norma)**(1/2)
    return norma
  def __add__(self,other):
          sumax=self.x+other.x
          sumay=self.y+other.y
          sumaz=self.z+other.z
          vectorsuma=Vector(sumax,sumay,sumaz)
          return vectorsuma
def suma_vectores(self,other):
      return self+other