class Ciudad:
  def __init__(self, x, y):
    self.x=float(x)
    self.y=float(y)
  def camino(self, other):
    x=(self.x+other.x)/2
    y=(other.y+self.y)/2
    return [[self.x,self.y],[x,y],[other.x,other.y]] 
  def distancia(self, other):
    x=other.x-self.x
    y=other.y-self.y
    return ((x*x+y*y)**(1/2))
         