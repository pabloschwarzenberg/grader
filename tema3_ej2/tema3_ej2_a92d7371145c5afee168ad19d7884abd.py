# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
  
  def norma(self):
    n=math.sqrt(self.x**2+self.y**2+self.z**2)
    return n
        
  def suma_vectores(self,v1,v2):
      v3=(v1.x+v2.x,v1.y+v2.y,v1.z+v2.z)
      return v3
      
  def __add__(self,other):
      v3=(self.x+other.x,self.y+other.y,self.z+other.z)
      return v3
