import math
class Ciudad:
  def __init__(self,x,y):
    self.x=x
    self.y=y
    self.pasos=[]
  def distancia(self,other):
    dx=abs(self.x-other.x)
    dy=abs(self.y-other.y)
    distancia=math.sqrt(dx**2+dy**2)
    return distancia
  def ca,imo(self,other):
    pass
if __name__ == "__main__":
  pass
         