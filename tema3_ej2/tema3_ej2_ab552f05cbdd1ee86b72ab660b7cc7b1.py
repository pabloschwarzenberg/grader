# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class vector:
  def __init__(self,x,y,z):
      self.x=x
      self.y=y
      self.z=z
  def norma (self):
      norma= math.sqrt(x**2+y**2+z**2)
  def __add__(self, other):
      v=vector(0,0,0)
      v.x=self.x+other.x
      v.y=self.y+other.y
      v.z=self.z+other.z
      return v
      
def suma_vectores(v1,v2):
   if type(v1) is vector and type(v2) is vector:
     v=v1+v2
     return v
   else:
        return False
