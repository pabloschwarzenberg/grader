import math
class Ciudad:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def camino(self, other):
    output = []
    while self.x != other.x and self.y != other.y:
      aux = [0, 0]
      if self.x - other.x > 0:
        aux[0] = self.x - 1
      elif self.x - other.x < 0:
        aux[0] = self.x + 1
      else:
        aux[0] = self.x      
        
      if self.y - other.y > 0:
        aux[1] = self.x - 1
      elif self.y - other.y < 0:
        aux[1] = self.y + 1
      else:
        aux[1] = self.y
      output.append(aux)
    return output
        
        
    
  def distancia(self, other):
    return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)

if __name__ == "__main__":
  p1=Ciudad(1,1)
  p2=Ciudad(3,3)
  p1.camino(p2)
  p1.distancia(p2)
         