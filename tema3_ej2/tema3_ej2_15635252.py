# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
  def __init__(self,x,y,z):
    self.x=int(x)
    self.y=int(y)
    self.z=int(z)
  def __add__(self, v):
        sumax = self.x + v.x
        sumay = self.y + v.y
        sumaz = self.z + v.z
        return (Vector(sumax, sumay, sumaz))
  def norma(self):
    if self.x==self.y==self.z:
       return(1)
    else:
       return ((self.x)**2+(self.z)**2+(self.y)**2)**(0.5)
def suma_vectores(self, v):
        sumax = self.x + v.x
        sumay = self.y + v.y
        sumaz = self.z + v.z
        return (Vector(sumax, sumay, sumaz))