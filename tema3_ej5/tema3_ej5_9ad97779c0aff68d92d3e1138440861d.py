class Ciudad:
  def __init__(self,x,y):
    self.x=x
    self.y=y
    
  def distancia(self,other):
      a=(self.x-other.x)**2
      b=(self.y-other.y)**2
      c=(a+b)**(0.5)
      return c
  
  def camino(self,other):
    camino=[]
    if self.x-other.x>0:
      x1=other.x
      while x1<self.x:
        camino.append([x1,other.y])
        x1=x1+1
        
    else:
      x1=self.x
      while x1<other.x:
        camino.append([x1,self.y])
        x1=x1+1
   
    if self.y-other.y>0:
       y1=other.y+1
       while y1<=self.y:
         camino.append([x1,y1])
         y1=y1+1
    else:
       y1=self.y+1
       while y1<=other.y:
         camino.append([x1,y1])
         y1=y1+1
  
    return camino
      
    

if __name__ == "__main__":
  pass
         