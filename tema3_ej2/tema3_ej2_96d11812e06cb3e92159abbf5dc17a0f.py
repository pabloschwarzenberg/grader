class Vector:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
  
  def norma(self):
    return (self.x**2 + self.y**2 + self.z**2)**0.5
  
  def __add__(self, vector2):
    return Vector(self.x + vector2.x, self.y + vector2.y, self.z + vector2.z)

  def __str__(self):
    return "({}, {}, {})".format(self.x, self.y, self.z)
      
def suma_vectores(vector1, vector2):
  return vector1 + vector2

if __name__ == "__main__":
  vector1 = Vector(1,2,3)
  vector2 = Vector(4,5,6)
  print(suma_vectores(vector1, vector2))
  