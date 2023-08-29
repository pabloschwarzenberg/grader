# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  def norma(self):
    norm = ((self.x)**2 + (self.y)**2 + (self.z)**2)**0.5
    return norm
  def suma_vectores(self, vec2):
    sumax = self.x + vec2.x
    sumay = self.y + vec2.y
    sumaz = self.z + vec2.z
    return "({},{},{})".format(sumax, sumay, sumaz)
    
vec1 = Vector(1,2,3)
vec2 = Vector(2,3,4)
print(vec1.norma())
print(vec1.suma_vectores(vec2))
           