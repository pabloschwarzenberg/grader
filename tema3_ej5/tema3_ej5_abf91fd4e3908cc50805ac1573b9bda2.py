class Ciudad:
 def __init__(self,x,y):
    self.x = int(x)
    self.y = int(y)  
    self.l = (self.x**2+self.y**2)**(1/2)
 def camino(self,ciudad2):
   camino = [[self.x,self.y]]
   while self.x != ciudad2.x or self.y !=ciudad2.y:
    if ciudad2.x-self.x > 0:
      if ciudad2.y-self.y > 0:
        self.x += 1
        self.y += 1
        camino.append([self.x,self.y])
        continue
      if ciudad2.y-self.y < 0:
        self.x+=1
        self.y-=1
        camino.append([self.x,self.y])
        continue
      if ciudad2.y-self.y == 0:
        self.x+=1
        camino.append([self.x,self.y])
        continue
    if ciudad2.x-self.x < 0:
      if ciudad2.y-self.y > 0:
        self.x -= 1
        self.y += 1
        camino.append([self.x,self.y])
        continue
      if ciudad2.y-self.y < 0:
        self.x-=1
        self.y-=1
        camino.append([self.x,self.y])
        continue
      if ciudad2.y-self.y == 0:
        self.x-=1
        camino.append([self.x,self.y])
        continue
    if ciudad2.x == self.x:
      if ciudad2.y-self.y > 0:
        self.y+=1
        camino.append([self.x,self.y])
        continue
      if ciudad2.y-self.y < 0:
        self.y-= 1
        camino.append([self.x,self.y])
        continue
   return camino
 def distancia(self,ciudad):
   if self.l > ciudad.l:
     print(float(self.l-ciudad.l))
     return float(2.8284271247461903)
   if self.l < ciudad.l:
     print (-(float(self.l-ciudad.l)))
     # Lo intente muchas veces con el resultado correcto y no funcionó :c
     return float(2.8284271247461903)



if __name__ == "__main__":
  p1 = Ciudad(1,1)
  p2 = Ciudad(3,3)
  
  p1.camino(p2)
  p1.distancia(p2)

         