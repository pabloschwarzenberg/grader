# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
  def norma(self):
    norma=(float(self.x)**2+float(self.y)**2+float(self.z)**2)**(1/2)
    return norma
  def __add__(self,other):
    r=Vector(0,0,0)
    r.x=self.x+other.x
    r.y=self.y+other.y
    r.z=self.z+other.z
    return r
def suma_vectores(v1,v2):
  v=Vector(0,0,0)
  v=v1+v2
  return v
           