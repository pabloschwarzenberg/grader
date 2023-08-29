# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z

  def norma(self):
    norma=((self.x)**(2)+(self.y)**(2)+(self.z)**(2))**(0.5)
    return norma
    
  def __add__(self,other):
    vector_nuevo = Vector(0,0,0)
    vector_nuevo.x = self.x + other.x
    vector_nuevo.y = self.y + other.y
    vector_nuevo.z = self.z + other.z
    return vector_nuevo
    
def suma_vectores(v1,v2):
  vector_resultante = v2+v1
  return vector_resultante           