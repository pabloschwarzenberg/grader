# crea la clase Vector y completa el código de la función suma_vectores usándola
def suma_vectores(v1,v2):
  vector=[]
  self.v1=v1
  self.v2=v2
  c=0
  for i in self.v1:
    coordenada=i + self.v2[c]
    vector.append(coordenada)
    c+=1
  return vector
def __modulo__(Vector):
  self.vector=Vector
  suma=0
  for i in self.vector:
    a=int(i)**2
    suma+=a
  suma=suma**(1/2)
  return suma
  