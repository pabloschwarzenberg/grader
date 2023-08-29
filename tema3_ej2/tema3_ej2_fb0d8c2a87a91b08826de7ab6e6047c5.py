# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
    
  def norma(self):
    a=(self.x)**2
    b=(self.y)**2
    c=(self.y)**2
    suma=a+b+c
    norma = math.sqrt(suma)
    return norma
    
  def __add__(self,v):
    sumax = self.x + v.x
    sumay = self.y + v.y
    sumaz = self.z + v.z
    vectorsuma= Vector(sumax,sumay,sumaz)
    return vectorsuma

def suma_vectores(v1,v2):
    vectorsuma= v1 + v2
    vectorsuma.x
    vectorsuma.y
    vectorsuma.z
    return vectorsuma
           