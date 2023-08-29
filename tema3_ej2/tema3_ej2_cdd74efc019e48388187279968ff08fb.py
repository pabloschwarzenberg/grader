# crea la clase Vector y completa el código de la función suma_vectores usándola
import math

#Clase Vector3D
class Vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
  
  def norma(self):
    a=(self.x)**2
    b=(self.y)**2
    c=(self.z)**2
    return((a+b+c)**(1/2))
  
  def __add__(self,other):
    l=self.x+other.x
    l1=self.y+other.y
    l2=self.z+other.z
    return Vector(l,l1,l2)
    
def suma_vectores(v1,v2):
  t=v1.x+v2.x
  i=v1.y+v2.y
  o=v1.z+v2.z
  return Vector(t,i,o)