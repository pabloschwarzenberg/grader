import math
class Ciudad:
  def __init__(self,p1,p2):
    self.p1 = p1
    self.p2 = p2
    
  def camino(self):
    c1=self.p1.split(',')
    c2=self.p2.split(',')
    c1x=c1[0]
    c1y=c1[1]
    c2x=c2[0]
    c2y=c2[1]
    dx=c2x-c1x
    dy=c2y-c1y
    return [p1,[dx,dy],p2]
    
  def distancia(self,dx,dy):
    distanciaentre= math.sqrt(dx**2 + dy**2)
    return distanciaentre
         