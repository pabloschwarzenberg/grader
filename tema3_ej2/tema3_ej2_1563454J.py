# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector:
    def __init__(self,a1,a2,a3):
        self.a1=a1
        self.a2=a2
        self.a3=a3
    def norma(self):
        norma=math.sqrt(self.a1**2+self.a2**2+self.a3**2)
        return norma
    def suma_vectores(self,v1,v2):
          v3=v1+v2
          return v3  
           