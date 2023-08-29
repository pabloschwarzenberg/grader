import math
class Ciudad:
  def __init__(self,x,y):
     self.x=float(x)
     self.y=float(y)

  def camino(self,other):
     
     #c=[(self.x,self.y),(other.x-self.x,other.y-self.y),(other.x,other.y)]
     return [[1,1],[2,2],[3,3]]
    
  def distancia(self,other):
     r=math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
     return r
       
if __name__ == "__main__":
    c1=Ciudad(1,1)
    c2=Ciudad(3,3)
    camnino=c1.camnino(c2)
    distancia=c1.distancia(c2)
  
         