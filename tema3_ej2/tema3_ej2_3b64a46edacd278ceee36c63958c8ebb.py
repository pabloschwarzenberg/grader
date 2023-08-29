# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
  def __init__(self,x,y,z):
    self.vector = [x,y,z]
    
  def __eq__(self,other):
    if(self.vector == other.vector):
      return True
    else: return False
    
  def __add__(self,other):
    if (len(self.vector == len(other.vector))):
      return(Vector(self.vector[0]+other.vector[0],self.vector[1]+other.vector[1],self.vector[2]+other.vector[3]))
  
  def norma(self):
    return((self.vector[0]**2+self.vector[1]**2+self.vector[2]**2)**(1/2))

  def suma_vectores(self,v1,v2):
    if (len(v1.vector == len(v2.vector))):
      return(Vector(v1.vector[0]+v2.vector[0],v1.vector[1]+v2.vector[1],v1.vector[2]+v2.vector[3]))
