# crea la clase Vector y completa el código de la función suma_vectores usándola
from math import sqrt
class Vector:
  def __init__(self,x,y,z): 
    self.x=x 
    self.y=y 
    self.z=z
    
  def __add__(self,otro):  
      c1=self.x+otro.x 
      c2=self.y+otro.y 
      c3=self.z+otro.z 
      return Vector(c1,c2,c3) 
    
  def norma(self):   
    norm=sqrt((self.x**2)+(self.y**2)+(self.z**2))
    return norm
    


def suma_vectores(v1,v2):   
  f1=v1.x+v2.x 
  f2=v1.y+v2.y 
  f3=v1.z+v2.z 
  return Vector(f1,f2,f3)
    
    
    
   
           