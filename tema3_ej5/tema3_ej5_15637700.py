from math import*

class Ciudad:
  def __init__(self, x, y):
      self.x = x
      self.y = y

  def camino(self, destino):
      cx = self.x
      cy = self.y
      camino = []
      camino.append([cx,cy])
      while cx!=destino.x or cy!=destino.y:
          if cx>destino.x:
              cx = cx - 1
          elif cx<destino.x:
              cx = cx + 1
          if cy>destino.y:
              cy = cy - 1
          elif cy<destino.y:
              cy = cy + 1
          camino.append([cx, cy])
      return camino

  def distancia(self, destino):
      a = int(self.x - destino.x)
      b = int(self.y - destino.y)
      c = float(sqrt(a**2+b**2))
      print(c)
      return c



if __name__ == "__main__":
    p1=Ciudad(1,1)
    p2=Ciudad(3,3)
    p1.camino(p2)
    p1.distancia(p2)
    p3=Ciudad(20,13)
    p4=Ciudad(22,-1)
    p3.camino(p4)
    p3.distancia(p4)
        
