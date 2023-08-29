class Ciudad:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def distancia(self, p2):
    suma_x = self.x - p2.x
    suma_y = self.y - p2.y

    distancia = (suma_x**2 + suma_y**2)**(0.5)
    return distancia    

  
  def camino(self, p2):
    self.punto = [self.x, self.y]
    self.camino = []
    self.camino.append(self.punto)
    x = self.x
    y = self.y

    while x != p2.x and y != p2.y:
      self.punto = []
      if x < p2.x:
        x += 1
      else:
        x -= 1
      if y < p2.x:
        y += 1
      else:
        y -= 1
      
      self.punto.append(x)
      self.punto.append(y)
      self.camino.append(self.punto)
      
    return self.camino
if __name__ == "__main__":
  pass
         