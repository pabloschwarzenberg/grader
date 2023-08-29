class Ciudad:
  def __init__(self,x,y):
    self.x=x
    self.y=y
    
  def camino(self,other):
    puntos=[[self.x,self.y]]
    d_x=other.x-self.x
    d_y=other.y-self.y
    if d_x>=d_y:
      diferencia=d_x-d_y
      proporcion=d_y
    else:
      diferencia=d_y-d_x
      proporcion=d_x
    for i in range(1,proporcion+1):
      puntos.append([self.x+i,self.y+i])
    if d_x>d_y:
      for i in range(1,diferencia+1):
        puntos.append([self.x+proporcion+i,self.y+proporcion])
    elif d_y>d_x:
      for i in range(1,diferencia+1):
        puntos.append([self.x+proporcion,self.y+proporcion+i])
    return puntos
  
  def distancia(self,other):
    d_x=other.x-self.x
    d_y=other.y-self.y
    if d_x>=d_y:
      diferencia=d_x-d_y
      proporcion=d_y
    else:
      diferencia=d_y-d_x
      proporcion=d_x
    d_proporcion=proporcion*(2**(1/2))
    d_diferencia=diferencia
    distancia_total=d_proporcion+d_diferencia
    return distancia_total
  

if __name__ == "__main__":
   p=input("Ingresa la primera ciudad (x,y): ")
   p=p.split(",")
   p1=Ciudad(int(p[0]),int(p[1]))
   p=input("Ingresa la segunda ciudad (x,y): ")
   p=p.split(",")
   p2=Ciudad(int(p[0]),int(p[1]))

         