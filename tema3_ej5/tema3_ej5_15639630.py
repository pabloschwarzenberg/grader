class Ciudad:

    def __init__(self, componenteX, componenteY):
        self.x = componenteX
        self.y = componenteY

    def distancia(self,a):
        b=((self.x-a.x)**2+(self.y-a.y)**2)**(1/2)
        return b

    def camino(self,a):
        r=[]
        X=self.x
        Y=self.y
        while X<a.x:
            m=int((a.y-Y)/(a.x-X))
            r.append ([X,Y])
            X=X+1
            Y=Y+m
        r.append ([a.x,a.y])
        return r

if __name__ == "__main__":
  print("La ciudad 1 es la que posee la coordenada x más pequeña")
  x=int(input("Ingrese la coordenada x de la ciudad 1"))
  y=int(input("Ingrese la coordenada y de la ciudad 1"))
  c1=Ciudad(x,y)
  print("")
  n=int(input("Ingrese la coordenada x de la ciudad 2"))
  m=int(input("Ingrese la coordenada y de la ciudad 2"))
  c2=Ciudad(n,m)

  print (Ciudad.camino(c1,c2))
  print("la distancia entre las dos ciudades es:",Ciudad.distancia(c1,c2))
         