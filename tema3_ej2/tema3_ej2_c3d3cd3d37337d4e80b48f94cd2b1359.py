# crea la clase Vector y completa el código de la función suma_vectores usándola
class vector:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
  def v1(self,norma):
    self.norma = (self.x**2 + self.y**2 + self.z**2)**(1/2)
           