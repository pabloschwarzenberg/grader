# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
  def norma(self):
    norma=((self.x)**2 + (self.y)**2 + (self.z)**2)**(1/2)
    return norma
  def suma_vectores(self,v1,v2):
    resultado_x=(v1.x+v2.x)
    resultado_y=(v1.y+v2.y)
    resultado_z=(v1.z+v2.z)
    v3=Vector(resultado_x,resultado_y,resultado_z)
    return v3
  def __add__(self,a,b):
    c=a+b
    d=Vector(a,b,c)
    return d             