class Ciudad:
  def __init__(self,x,y):
    self.x=x
    self.y=y
  def camino(self,other):
    pasos=[[self.x,self.y]]
    pasos.append([other.x,other.y])
    return pasos
  def distancia(self,other):
    import math
    return math.sqrt(((other.x-self.x)**2)+((other.y-self.y)**2))
       