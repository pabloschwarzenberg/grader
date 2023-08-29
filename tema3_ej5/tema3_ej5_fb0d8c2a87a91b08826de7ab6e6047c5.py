import math
class Ciudad:
  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.puntos=[x,y]
    
  def puntos(self,other):
    punnto2=other.x - self.x,other.y - self.y
    puntos=[]
    puntos.append(self.puntos)
    puntos.append(punnto2)
    puntos.append(other.puntos)
    return puntos
   
  def camino(self,other):
    a = self.x - other.x
    b = self.y - other.y
    distancia = math.sqrt(a**2+b**2)
    return distancia


    