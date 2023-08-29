# crea la clase Vector y completa el código de la función suma_vectores usándola
import math
class Vector:
  def __init__(self,vector):
    self.vector=vector
  def __add__(self,other):
    i=0
    x=[]
    while i<len(self.vector):
      a=(int(self.vector[i])+int(other.vector[i]))
      x.append(a)
      i=i+1
    self.vector=x
    return self.vector
  def norma(self):
    i=0
    v=[]
    while i<len(self.vector):
      parametro=(int(self.vector[i]))**2
      v.append(parametro)
      i=i+1
    norm=math.sqrt(sum(v))
    return norm
def suma_vectores(v1,v2):
  i=0
  nuevo_vector=[]
  while i<len(v1):
    parametro_k=(int(v1[i])+int(v2[i]))
    nuevo_vector.append(parametro_k)
    i=i+1
  self.vector=nuevo_vector
  return nuevo_vector
           