# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
    
  def __add__(self,v2):
    v2=Vector(0,0,0)
    x3=self.x+v2.x
    y3=self.y+v2.y
    z3=self.z+v2.z
    resultado=Vector(x3,y3,z3)
    return resultado 
   
  def __mod__(self):
    a=self.x*self.x
    b=self.y*self.y
    c=self.z*self.z
    norma=(a+b+c)**(1/2)
    return norma
    