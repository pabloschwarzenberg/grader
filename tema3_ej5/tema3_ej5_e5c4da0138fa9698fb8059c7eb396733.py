class Ciudad:
  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.puntos = []
  def camino(self, ciudad):
    for i in range(self.x, ciudad.x+1):
      self.puntos.append([i,i])
    return self.puntos
  def distancia(self, ciudad):
    return ((ciudad.x - self.x)**2+(ciudad.y - self.y)**2)**0.5
    
  

if __name__ == "__main__":
  p1=Ciudad(1,1)
  p2=Ciudad(3,3)
  p1.camino(p2)
         