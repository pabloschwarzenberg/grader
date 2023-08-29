import math
class Ciudad:
  def __init__(self,p1,p2):
     self.p1=p1
     self.p2=p2
     
  def camino(self,numero):
     y=numero.p2-self.p2
     x=numero.p1-self.p1
     m=y/x
     camino=[]
     for i in range(self.p1,numero.p1+1):
        y2=m*i-m*self.p1+self.p2
        punto=[i,y2]
        camino.append(punto)
     return camino
     
  
  
  def distancia(self,posicion):
    dist=math.sqrt((posicion.p1-self.p1)**2+(posicion.p2-self.p2)**2)
    return dist
     
     

if __name__ == "__main__":
  p1=str(input("Ingrese ciudad 1"))
  p2=str(input("Ingrese ciudad 2"))
  p1=Ciudad(p1)
  p2=Ciudad(p2)
  print(p1.camino(p2))
  print(p1distancia(p2))