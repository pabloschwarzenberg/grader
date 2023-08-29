# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
  
  def norma(self):
    cuadrado1=(self.x)**2
    cuadrado2=(self.y)**2
    cuadrado3=(self.z)**2
    raiz=math.sqrt(cuadrado1+cuadrado2+cuadrado3)
    return raiz
    
  def __add__(self,other):
    r=Vector(0,0,0)
    r.x=self.x+other.x
    r.y=self.y+other.y
    r.z=self.z+other.z
    return r

def suma_vectores(v1,v2):
    vf=v1+v2
    return vf
           