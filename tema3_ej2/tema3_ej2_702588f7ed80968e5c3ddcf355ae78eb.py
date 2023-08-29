# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
    def __init__(self, d1, d2, d3):
        self.d1=float(d1)
        self.d2=float(d2)
        self.d3=float(d3)
    def norma(self,d1,d2,d3):
      self.norma=(self.d1**2+self.d2**2+self.d3**2)**0.5
      return self.norma
    def __str__(self):
        return "la norma es:" , "{0}".format(self.norma)
v1=Vector (1,2,2)
norma1=v1.norma
print(norma1)

def suma_vectores(v1,v2):
  return
           