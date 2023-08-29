# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
    self.norm = self.norma()
  def norma(self):
    return (math.sqrt((self.x**2)+(self.y**2)+(self.z**2)))    
  def __add__(self,v2):
     return suma_vectores(self, v2)
     
def suma_vectores(self, v2):
    nuevo = Vector(0,0,0)
    nuevo.x = self.x + v2.x
    nuevo.y=self.y+v2.y
    nuevo.z=self.z+v2.z
    return nuevo
           