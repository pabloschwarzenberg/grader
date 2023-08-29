def punto(x1,y1,x2,y2):
  pendiente = (x1 - x2)/(y1 - y2)
  corte = -pendiente*x1
  y = pendiente*x1 + corte
  x = (y1 - corte)/(pendiente)
  puntos = [x,y]
  return puntos  

class Ciudad:
  def __init__(self,x,y):
    self.x = x
    self.y = y

  def distancia(self, other):
    distancia = ((self.x - other.x)**2 + (self.y - other.y)**2)**(1/2)
    return distancia
    
  def camino(self, other):
    camino = []    
    i = 0
    camino.append([self.x,self.y])
    while i < abs(self.x - other.x):
      camino.append(punto(self.x + i,punto(self.x + i,self.y,other.x,other.y)[1],other.x,other.y))
      i += 1
    camino.append([other.x,other.y])
    return camino
    
if __name__ == "__main__":
  pass
         