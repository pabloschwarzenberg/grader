# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector:
    def __init__(self,x1,x2,x3):
        self.x1=x1
        self.x2=x2
        self.x3=x3
    def norma(self):
        norma=math.sqrt((self.x1**2)+(self.x2**2)+(self.x3**2))
        return norma
    def __add__(self,v2):
        x1=self.x1+v2.x1
        x2=self.x2+v2.x2
        x3=self.x3+v2.x3
        return Vector(x1,x2,x3)
    def __repr__(self):
        return Vector(self.x1,self.x2,self.x3)
def suma_vectores(v1,v2):
  suma=v1+v2
  return suma
           