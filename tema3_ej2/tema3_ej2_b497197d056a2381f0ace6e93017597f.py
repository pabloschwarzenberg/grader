class Vector():
  def __init__(self, x, y, z):
    self.x = x 
    self.y = y
    self.z = z 
    
  def norma(self):
    return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** (1/2)
    
  def __add__ (self, otro):
    return Vector(self.x + otro.x, self.y + otro.y, + self.z + otro.z)

# crea la clase Vector y completa el código de la función suma_vectores usándola
def suma_vectores(v1,v2):
  return v1 + v2
           