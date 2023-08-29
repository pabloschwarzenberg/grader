import math

class Ciudad:
  def __init__(self,x,y):
    self.x=x
    self.y=y
  
  def distancia(self,other):
    d2=(self.x-other.x)**2+(self.y-other.y)**2
    d=math.sqrt(d2)
    return d
  
  def camino(self,other):
    def eqrect(x,a=self,b=other):
      m=(b.y-a.y)/(b.x-a.x)
      y=int(m*(x-a.x)+a.y)
      return y
    pasos=[]
    for i in range(self.x,other.x+1):
      paso=[i,eqrect(i)]
      pasos.append(paso)
    return pasos

if __name__ == "__main__":
  p1=Ciudad(1,1)
  p2=Ciudad(3,3)
  print(p1.camino(p2))
  print(p1.distancia(p2))
         