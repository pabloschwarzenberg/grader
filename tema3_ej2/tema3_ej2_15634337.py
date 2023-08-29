# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector:
    def __init__(self,n1,n2,n3):
        self.n1=n1
        self.n2=n2
        self.n3=n3
    def norma(self):
        norm = math.sqrt((self.n1**2)+(self.n2**2)+(self.n3**2))
        return norm
    def __add__(self, other):
        s1=self.n1+other.n1
        s2=self.n2+other.n2
        s3=self.n3+other.n3
        respuesta=(s1,s2,s3)
        return respuesta
    def __repr__(self):
      a=(self.n1,self.n2,self.n3)
      return a
def suma_vectores(v1,v2):
  v3=v1+v2
  return v3
           