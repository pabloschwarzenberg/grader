import math
class Ciudad:
  def __init__(self,x,y):
    self.x=x
    self.y=y
  def camino(self,other):
    self.lista=[[self.x,self.y]]
    x_2=other.x
    y_2=other.y
    while (x_2!=self.x) or (y_2!=self.y):
      if x_2!=self.x:
        self.x=self.x+1
      if y_2!=self.y:
        self.y=self.y+1
        
      a=[self.x,self.y]
      self.lista.append(a)
    print(self.lista)
  def distancia(self,other):
    d=len(self.lista)
    distancia=0
    for i in range(1,d):
      a=self.lista[i-1][0]
      a_1=self.lista[i][0]
      b=self.lista[i-1][1]
      b_1=self.lista[i][1]
      x=(a-a_1)**2
      y=(b-b_1)**2
      distancia=math.sqrt(x+y)+distancia
    print(distancia)
      
    

if __name__ == "__main__":
  pass
         