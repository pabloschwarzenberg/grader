class Ciudad(object):
  x = 0
  y = 0
  distancia = 0

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.distancia = 0

  def camino(self, otra_ciudad):
    print('Camino:')
    # Implementar
    return None

  def distancia(self, otra_ciudad):
    # Implementar
    return 0

p1=Ciudad(1,1)
p2=Ciudad(3,3)
p1.camino(p2)

p1.distancia(p2)