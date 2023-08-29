class Ciudad:
  def __init__(self,x,y):
    self.x=x
    self.y=y
  def camino(self,other):
    return[[self.x,self.y],[(other.x-self.x),(other.y-self.y)],[other.x,other.y]]
  def distancia(self,other):
    return ((other.y-self.y)**2+(other.x-self.y)**2)**0.5

if __name__ == "__main__":
  p1=Ciudad(1,1)
  p2=Ciudad(3,3)
  print(p1.camino(p2),"",p1.distancia(p2))
         