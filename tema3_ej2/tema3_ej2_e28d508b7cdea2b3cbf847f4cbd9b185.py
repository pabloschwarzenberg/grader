# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
    self.vector=(self.x,self.y,self.z)
  def norma(self):
    norma=math.sqrt((float(self.x)*float(self.x))+(float(self.y)*float(self.y))+(float(self.z)*float(self.z)))
    return norma
  def __add__(self,valor):
    r=Vector(0,0,0)
    r.x=self.x+valor.x
    r.y=self.y+valor.y
    r.z=self.z+valor.z
    return r
  
def suma_vectores(v1,v2):
  suma=[(int(v1.x)+int(v2.x)),(int(v1.y)+int(v2.y)),(int(v1.z)+int(v2.z))]
  return Vector(suma[0],suma[1],suma[2])
  