# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector:
  def __init__(self):
    self.componentes=[0,0,0]
  def norma(self):
    return math.sqrt((self[0]**2)+(self[1]**2)+(self[2]**2))

    
def suma_vectores(v1,v2):
  a=v1[0]+v2[0]
  b=v1[1]+v2[1]
  c=v1[2]+v2[2]
  return [a,b,c]
           