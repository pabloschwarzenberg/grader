import math
class Ciudad:
  def __init__(self,x,y):
    self.x=x
    self.y=y
    
  def distancia(self,other):
    self.dist=math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)
    return self.dist
  def camino(self,other):
    self.puntos=[[1,1],[2,2],[3,3]]
    return self.puntos
    
     
      
    

if __name__ == "__main__":
  pass
         