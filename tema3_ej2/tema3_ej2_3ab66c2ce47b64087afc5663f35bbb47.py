# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:

  def __init__(self,x,y,z):
    self.x = x
    self.y = y
    self.z = z
  
  def norma(self):
    norma = (self.x**2+self.y**2+self.z**2)**(1/2)
    return norma

  def __add__(a,b):
    v3 = Vector(a.x+b.x,a.y+b.y,a.z+b.z) 
    return v3
    
def suma_vectores(v1,v2):
  v3 = Vector(v1.x+v2.x,v1.y+v2.y,v1.z+v2.z) 
  return v3
  
           