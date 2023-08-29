import math
class Ciudad:
  def __init__(self,x,y):
    self.x=x
    self.y=y
    
  def camino(self,other):
    camino=[[self.x,self.y],[abs(self.x+other.x),abs(self.y+other.y)],[other.x,other.y]]
    return camino
   
  def distancia(self,other):
    distancia=math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)
    return float(distancia)
if __name__ == "__main__":
  pass
         