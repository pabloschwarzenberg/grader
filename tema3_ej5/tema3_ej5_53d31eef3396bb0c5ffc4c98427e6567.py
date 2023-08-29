import math
from math import sqrt
class Ciudad:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  pass
  def distancia(self, p2):
    return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
    
  def camino(self, punto2):
    camino=[]
    puntox= 0
    puntoy= 0
    punto1 = [p1.x,p1.y]
    punto2 = [p2.x,p2.y]
    posicion = punto1
    camino.append(punto1[:])
    while posicion[0] != punto2[0] or posicion[1] != punto2[1]:
      if punto1[0]<punto2[0]:
        puntox = (punto1[0]+1)
        if punto1[1]<punto2[1]:
          puntoy = (punto1[1]+1)
        elif punto1[1]>punto2[1]:
          puntoy = (punto1[1]-1)
        elif punto1[1]==punto2[1]:
          puntoy = (punto1[1])
      elif punto1[0]>punto2[0]:
        puntox = (punto1[0]-1)
        if punto1[1]<punto2[1]:
          puntoy = (punto1[1]+1)
        elif punto1[1]>punto2[1]:
          puntoy = (punto1[1]-1)
        elif punto1[1]==punto2[1]:
          puntoy = (punto1[1])
      elif punto1[0]==punto2[0]:
        puntox = (punto1[0])
        if punto1[1]<punto2[1]:
          puntoy = (punto1[1]+1)
        elif punto1[1]>punto2[1]:
          puntoy = (punto1[1]-1)
        elif punto1[1]==punto2[1]:
          puntoy = (punto1[1])
      posicion[0]=puntox
      posicion[1]=puntoy
      camino.append(posicion[:])
    return camino

if __name__ == "__main__":
  pass
        
p1 = Ciudad(1,1)
p2 = Ciudad(3,3)

print(p1.camino(p2))
Distancia = p1.distancia(p2)
print(Distancia// 0.01 / 100)