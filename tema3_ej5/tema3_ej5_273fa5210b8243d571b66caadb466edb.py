import math as m
def lineal(p1, p2):
  m = (p2[1] - p1[1]) / (p2[0] - p1[0])
  n = p1[1] - m*p1[0]
  rec = []
  for x in range(p1[0], p2[0] + 1):
    y = m*x + n
    rec.append([x,y])
  return rec

class Ciudad:
  def __init__(self,x,y):
      
      self.x = int(x)
      self.y = int(y)
      self.xy = [int(x), int(y)]
  
  def camino(self, otra):
    c = lineal(self.xy, otra.xy)
    return c
  
  def distancia(self, otra):
      d = m.sqrt((self.x - otra.x)**2 + (self.y - otra.y)**2)
      return d

if __name__ == "__main__":
  pass
         