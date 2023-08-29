class Ciudad:
  def __init__(self, x,y):
      self.x=x
      self.y=y
  def distancia(self, other):
      x= self.x-other.x
      y= self.y-other.y
      return (x**2+y**2)**0.5
  def camino(self, other):
      return  [[self.x,self.y],[other.x-self.x,other.y-self.y],[other.x,other.y]]

if __name__ == "__main__":
  p1.distancia(p2)
         