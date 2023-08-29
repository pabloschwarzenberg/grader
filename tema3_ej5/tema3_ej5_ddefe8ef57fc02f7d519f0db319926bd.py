import math
class Ciudad:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def distancia(self, other):
    dx = other.x - self.x
    dy = other.y - self.y
    return math.sqrt(dx * dx + dy * dy)
  def camino(self, other):
    a, b = self.x , self.y
    c, d = other.x, other.y
    l = [[a, b]]
    while a < c and b < d:
      l.append([a + 1,b + 1])
      a += 1
      b += 1
    return l
  
if __name__ == "__main__":
  pass
         