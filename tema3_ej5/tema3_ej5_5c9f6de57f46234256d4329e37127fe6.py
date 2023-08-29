import math
class Ciudad:
  def __init__(self,x,y):
    self.x = float(x)
    self.y = float(y)
    meow = []
  def camino(self,other):
    c=[[self.x,self.y],[(self.x-other.x),(self.y-other.y)],[other.x,other.y]]
    return c
  def distancia(self,other):
    d=math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)
    return d
if __name__ == "__main__":
  pass
         