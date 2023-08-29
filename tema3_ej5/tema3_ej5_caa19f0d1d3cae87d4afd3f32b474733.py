import math

class Ciudad:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def camino(self, otra_ciudad):
    camino = []
    current_x = self.x
    current_y = self.y
    
    while current_x != otra_ciudad.x or current_y != otra_ciudad.y:
      camino.append([current_x, current_y])
      if current_x < otra_ciudad.x:
        current_x += 1
      elif current_x > otra_ciudad.x:
        current_x -= 1
        
      if current_y < otra_ciudad.y:
        current_y += 1
      elif current_y > otra_ciudad.y:
        current_y -= 1
        
    camino.append([current_x, current_y])
    return camino
    
  def distancia(self, otra_ciudad):
    distancia_x = otra_ciudad.x - self.x
    distancia_y = otra_ciudad.y - self.y
    distancia = math.sqrt(distancia_x**2 + distancia_y**2)
    return round(distancia, 16)
    
p1 = Ciudad(1,1)
p2 = Ciudad(3,3)

ruta = p1.camino(p2)
distancia = p1.distancia(p2)

print("Ruta:", ruta)
print("Distancia:", distancia)
         