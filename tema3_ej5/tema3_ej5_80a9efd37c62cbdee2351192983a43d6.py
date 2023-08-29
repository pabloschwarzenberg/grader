import math
class Ciudad:
  def __init__(self,x,y):
      self.x=x
      self.y=y
  def camino(self, other):
      h=[]
      pc=[]
      p2=[]
      pasos=[]
      pntomedx= abs(self.x - other.x)/2
      pntomedy= abs(self.y - other.y)/2
      h.append(pntomedx)
      h.append(pntomedy)
      pc.append(self.x)
      pc.append(self.y)
      p2.append(other.x)
      p2.append(other.y)
      pasos.append(pc)
      pasos.append(h)
      pasos.append(p2)
      return pasos

  def distancia(self, other):
      dist= math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
      return dist

if __name__ == "__main__":
  p1 = Ciudad(1,1)
  p2 = Ciudad(3,3)
  p1.camino(p2)
  p1.distancia(p2)
         