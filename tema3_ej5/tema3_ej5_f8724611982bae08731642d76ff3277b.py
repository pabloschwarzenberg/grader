class Ciudad:
  def __init__(self,x,y):
    self.x=x
    self.y=y
    self.x_final=0
    self.y_final=0
  def camino(self,other):
    self.x_final=other.x-self.x
    self.y_final=other.y-self.y
    return [[self.x,self.y], [self.x_final,self.y_final], [other.x,other.y]]
  def distancia(self,camino):
    x=((int(self.x_final))**2+(int(self.y_final))**2)**(1/2)
    return x
  def __str__(self):
    return self.x, self.y
    
    
  
  pass

if __name__ == "__main__":
  pass
         