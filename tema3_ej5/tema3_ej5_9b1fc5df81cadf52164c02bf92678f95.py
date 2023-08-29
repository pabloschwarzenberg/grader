class Ciudad:
  def __init__(self,x,y):
    self.pasos = [[x,y]]
    self.x = x
    self.y = y
    self.coordenada = [self.x,self.y]
    self.dist = 0
    
  def camino(self,p2):
    self.X = self.x
    self.Y = self.y
    while self.X!=p2.x and self.Y!=p2.y:
      if self.X!=p2.x:
        self.X += 1
      if self.Y!=p2.y:
        self.Y += 1
      self.pasos.append([self.X,self.Y])
    return self.pasos
  
  def distancia(self,p2):
    self.dist = self.dist + ((((p2.x-self.x)**2)+((p2.y-self.y)**2))**0.5)
    return self.dist
    

if __name__ == "__main__":
  pass
         