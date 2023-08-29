# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
  def norma(self):
    n=(((float(self.x))**2)+((float(self.y))**2)+((float(self.z))**2))**(1/2)
    return n
  def __add__(self,other):
    return(suma_vectores(self,other))
def suma_vectores(v1,v2):
  d=Vector(0,0,0)
  d.x=v1.x+v2.x
  d.y=v1.y+v2.y
  d.z=v1.z+v2.z
  d=Vector(d.x,d.y,d.z)
  return d