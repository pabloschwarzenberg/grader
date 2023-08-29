import math
class Ciudad:
  def __init__(self,x,y):
    self.x=float(x)
    self.y=float(y)
    
  def camino(self,other):
    y=[[self.x,self.y],[(self.x  -other.x),(self.y - other.y)],[other.x,other.y]]
    return y
  
  def distancia(self,other):
    distance=math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)
    return distance
if __name__ == "__main__":
  pass
         