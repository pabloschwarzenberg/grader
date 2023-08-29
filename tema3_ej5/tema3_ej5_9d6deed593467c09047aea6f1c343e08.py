class Ciudad:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __repr__(self):
    return "[" + str(self.x) + ", " + str(self.y) + "]"

  def distancia(self, otra_ciudad):
    return ((otra_ciudad.x - self.x)**2 + (otra_ciudad.y - self.y)**2)**0.5

  def camino(self, otra_ciudad):
    paso_x = 1 if otra_ciudad.x > self.x else -1
    paso_y = 1 if otra_ciudad.y > self.y else -1
    camino = []
    while self.x != otra_ciudad.x or self.y != otra_ciudad.y:
      self.x += paso_x
      self.y += paso_y
      camino.append([self.x, self.y])
    print(camino)
    print("Distancia recorrida:", round(self.distancia(otra_ciudad), 2))
    
