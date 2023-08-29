class Vector:
  def __init__(self,x,y,z):
    self.x = x
    self.y = y
    self.z = z
  def norma(self):
    norma = (self.x**2 + self.y**2 + self.z**2)**(1/2)
    return norma
  def __add__(self, v1):
    x1 = self.x+v1.x
    y1 = self.y+v1.y
    z1 = self.z+v1.z
    return Vector(x1,y1,z1)
    
# crea la clase Vector y completa el código de la función suma_vectores usándola
def suma_vectores(v1,v2):
  v3 = v1 + v2
  
  return v3
           