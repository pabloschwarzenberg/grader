# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector():
  def __init__(self,x,y,z):
    self.cordx=x
    self.cordy=y
    self.cordz=z
  def norma(self):
    norma=(int(self.cordx)**2+int(self.cordy)**2+int(self.cordz)**2)**(1/2)
    self.norma=norma
    return norma

           