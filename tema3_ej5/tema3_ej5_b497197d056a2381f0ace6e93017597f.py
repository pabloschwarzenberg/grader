class Ciudad:
  def __init__ (self, x, y):
    self.x, self.y = x, y 
  
  def distancia(self, otra):
    d = ((self.x - otra.x) ** 2 + (self.y - otra.y) ** 2) ** (1/2)
    return d
    
  def camino(self, otra):
    self.caminox = [[self.x, self.y]]
    if self.x < otra.x:
      factor = 1
    elif self.x > otra.x: 
      factor = -1
    x1 = self.x
    while x1 != otra.x:
      x1 = x1 + factor 
      self.caminox.append([x1, self.y])
          
    if self.y < otra.y:
     factor = 1  
    elif self.y > otra.x: 
      factor = -1
    y1 = self.y
    while y1 != otra.y:
      y1 = y1 + factor 
      self.caminox.append([x1, y1])
    
    return self.caminox
     

if __name__ == "__main__":
  pass
         