import math
class Ciudad:
  def __init__(self,x,y):
    self.x=x
    self.y=y
  def camino(self,other):
    camino=[]
    if self.x==other.x:
      diferencia=int(self.y)-int(other.y)
      for i in range(diferencia+1):
        lista=[self.x,self.y+1]
        camino.append(lista)
      return camino
    elif self.y==other.y:
      diferencia=int(self.x)-int(other.x)
      for i in range(diferencia+1):
        lista=[self.x+i,self.y]
        camino.append(lista)
      return camino
    else:
      diferencia_x=abs(int(self.x)-int(other.x))
      diferencia_y=abs(int(self.y)-int(other.y))
      for i in range(diferencia_x+1):
        lista1=[self.x+i,self.y]
        camino.append(lista1)
      for i in range(1,diferencia_y+1):
        lista=[self.x+diferencia_x,self.y+i]
        camino.append(lista)
      return camino
  def distancia(self,other):
      calculo=((int(self.x)-int(other.x))**2)+((int(self.y)-int(other.y))**2)
      distancia=math.sqrt(calculo)
      return distancia
if __name__ == "__main__":
  pass
         