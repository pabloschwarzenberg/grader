# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
    def __init__(self,x,y,z):
      self.x=x
      self.y=y
      self.z=z
    def norma(self):
      norma=(self.x**2+self.y**2+self.z**2)**(1/2)
      return norma
    def __repr__(self):
        a="({},{},{})".format(self.x,self.y,self.z)
        return a
    def __add__(self,other):
      c=Vector(0,0,0)
      c.x=self.x+other.x
      c.y=self.y+other.y
      c.z=self.z+other.z
      return c
def suma_vectores(v1,v2):
  return v1+v2           