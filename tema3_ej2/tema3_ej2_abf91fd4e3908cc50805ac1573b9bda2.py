class Vector:
  def __init__(self,x,y,z):
    self.x = x
    self.y = y
    self.z = z
  def norma(self):
    return ((self.x**2)+(self.y**2)+(self.z**2))**(1/2)
  
  def __add__(self,v1):
      return suma_vectores(self,v1)

    
def suma_vectores(v1,v2):
    vector_suma = Vector(0,0,0)
    vector_suma.x = v1.x + v2.x
    vector_suma.y = v1.y + v2.y
    vector_suma.z = v1.z + v2.z
    return vector_suma

    
    
    