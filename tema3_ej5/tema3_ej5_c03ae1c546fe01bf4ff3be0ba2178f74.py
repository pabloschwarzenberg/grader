import math
class Ciudad:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  pass
  def camino(self,other):
    x=self.x
    y=self.y
    camino = [[self.x,self.y],[other.x,other.y]]
    for d in range(int(((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** (1 / 2))):
      if x < other.x:
        x +=1
      if x > other.x:
        x-=1
      if y < other.y:
        y +=1
      if y > other.y:
        y -= 1
      camino.insert(-1,[x,y])
    return camino
  def distancia(self, other):
    return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** (1 / 2)
if __name__ == "__main__":
  pass
         