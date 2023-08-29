import math

class Ciudad:
  
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def camino(self, ciudad):
    x1, y1 = self.x, self.y
    x2, y2 = ciudad.x, ciudad.y
    
    dx = x2 - x1
    dy = y2 - y1
    
    # Calcula la distancia a recorrer
    distancia = math.sqrt(dx**2 + dy**2)
    
    # Calcula los pasos necesarios
    pasos = []
    pasos.append([x1, y1])
    for i in range(1, int(distancia)+1):
      x = round(x1 + i*dx/distancia)
      y = round(y1 + i*dy/distancia)
      pasos.append([x, y])
    pasos.append([x2, y2])
    
    print(pasos)
    return pasos
  
  def distancia(self, ciudad):
    x1, y1 = self.x, self.y
    x2, y2 = ciudad.x, ciudad.y
    
    dx = x2 - x1
    dy = y2 - y1
    
    # Calcula la distancia a recorrer
    distancia = math.sqrt(dx**2 + dy**2)
    
    print(distancia)
    return distancia

# Ejemplo de uso
if __name__ == "__main__":
  coor1 = input("Ingrese las coordenadas de la primera ciudad separadas por una coma: ")
  coor2 = input("Ingrese las coordenadas de la segunda ciudad separadas por una coma: ")
  x1, y1 = map(float, coor1.split(','))
  x2, y2 = map(float, coor2.split(','))
  
  p1 = Ciudad(x1, y1)
  p2 = Ciudad(x2, y2)
  
  p1.camino(p2)
  p1.distancia(p2)

