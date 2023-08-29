class Ciudad:
    def __init__(self,x,y):
        self.cordx=int(x)
        self.cordy=int(y)
    def camino(self,ciudad2):
        posx=self.cordx
        posy=self.cordy
        actual=[posx,posy]
        pasos=[actual]
        while posx!=ciudad2.cordx or posy!=ciudad2.cordy:
            if posx>ciudad2.cordx:
                posx-=1
            elif posx<ciudad2.cordx:
                posx+=1
            if posy>ciudad2.cordy:
                posy-=1
            elif posy<ciudad2.cordy:
                posy+=1
            actual=[posx,posy]
            pasos.append(actual)
        return pasos
    def distancia(self,ciudad2):
        distancia=((ciudad2.cordx-self.cordx)**2 + (ciudad2.cordy-self.cordy)**2)**(1/2)
        return(distancia)

if __name__ == "__main__":
  x=int(input("Coordenada x de la primera ciudad: "))
  y=int(input("Coordenada y de la primera ciudad: "))
  p1=Ciudad(x,y)
  x=int(input("Coordenada x de la segunda ciudad: "))
  y=int(input("Coordenada y de la segunda ciudad: "))
  p2=Ciudad(x,y)
  r=p1.camino(p2)
  print(r)
  d=p1.distancia(p2)
  print(d)







         