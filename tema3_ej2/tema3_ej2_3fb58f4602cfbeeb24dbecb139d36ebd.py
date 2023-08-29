# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
  def __init__(self,x,y,z):
      self.x=x
      self.y=y
      self.z=z
  def norma(self):
    cuadrado=(self.x)**2+(self.y)**2+(self.y)**2
    norma_vector=(cuadrado)**(1/2)
    return norma_vector
  def __add__(self,other):
    if isinstance(self,Vector)==True:
      if isinstance(other,Vector)==True:
        x_nuevo=self.x+other.x
        y_nuevo=self.y+other.y
        z_nuevo=self.z+other.z
        Vector(x_nuevo,y_nuevo,z_nuevo)
        return Vector(x_nuevo,y_nuevo,z_nuevo)
    
def suma_vectores(self,other):
    return self+other
 
  
           