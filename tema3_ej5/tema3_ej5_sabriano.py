import math
class Ciudad:
  def __init__(self,x,y):
    self.x=x
    self.y=y
    self.puntosx=[]
    self.puntosy=[]
    self.camino=[]
  def camino(self,other):
    while other.x>self.x:
     self.puntosx=[]
     self.puntosx.append(self.x)
     self.puntosx.append(self.y)
     self.x=self.x+1
     self.camino.append(self.puntosx)
    while other.y>self.y:
      self.puntosy=[]
      self.puntosy.append(self.x)
      self.puntosy.append(self.y)
      self.y=self.y+1
      self.camino.append(self.puntosy)
    return self.camino
  def distancia(self,other):
    distancia=math.sqrt(((other.x-self.x)**2)+((other.y-self.y)**2))
    return distancia

if __name__ == "__main__":
  pass
         