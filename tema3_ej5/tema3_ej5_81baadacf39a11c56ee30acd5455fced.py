import math
class Ciudad:
  def __init__(self,x,y):
      self.posx=x
      self.posy=y
      
  def camino(self,city):
      x=self.posx
      y=self.posy
      i=1 #por default las coordenadas de la ciudad de destino son mayores a las coordenadas de la ciudad de inicio
      j=1
      road = [ [x, y] ]
      if city.posx < self.posx:
        i=-1
      if city.posy < self.posy:
        j=-1
      while x != city.posx:
        x=x+i
        road.append([x,y])
      while y != city.posy:
        y=y+j
        road.append([x,y])
      return road

      
    
  def distancia(self,city):
      #math.sqrt((self.ciudad2[0]-self.ciudad1[0])**2+(self.ciudad2[1]-self.ciudad1[1])**2)
      return math.sqrt((city.posx-self.posx)**2+(city.posy-self.posy)**2)

if __name__ == "__main__":
    p1=Ciudad(1,5)
    p2=Ciudad(3,3)
    d=p1.distancia(p2)
    print(d)
    r=p1.camino(p2)
    print(r)