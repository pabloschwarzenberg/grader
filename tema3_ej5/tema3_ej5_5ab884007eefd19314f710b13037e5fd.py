class Ciudad:
  def __init__(self,x,y):
    self.x=x
    self.y=y
  
  def distancia(self,other):
    distancia=(((float(other.x)-float(self.x))**2)+((float(other.y)-float(self.y))**2))**(1/2)
    return distancia
  
  def camino(self,other):
    camino=[]
    camino.append([self.x,self.y])
    x=self.x
    y=self.y
    while x!=other.x or y!=other.y:
      if self.x!=other.x:
        if self.x<other.x:
          x=x+1
        elif self.x>other.x:
          x=x-1
      if self.y!=other.y:
        if self.y<other.y:
          y=y+1
        elif self.y>other.y:
          y=y-1
      camino.append([x,y])
    return camino
      
        
          