class Ciudad:
    def __init__(self,x,y):
        self.cordenada_x=int(x)
        self.cordenada_y=int(y)
    def camino(self,ciudad_dos):
        posicion_x=self.cordenada_x
        posicion_y=self.cordenada_y
        actual=[posicion_x,posicion_y]
        pasos=[actual]
        while posicion_x!=ciudad_dos.cordenada_x or posicion_y!=ciudad_dos.cordenada_y:
            if posicion_x>ciudad_dos.cordenada_x:
                posicion_x=1-posicion_x
            elif posicion_x<ciudad_dos.cordenada_x:
                posicion_x=1+posicion_x
            if posicion_y>ciudad_dos.cordenada_y:
                posicion_y=1-posicion_y
            elif posicion_y<ciudad_dos.cordenada_y:
                posicion_y=1+posicion_y
            actual=[posicion_x,posicion_y]
            pasos.append(actual)
        return pasos
    def distancia(self,ciudad_dos):
        distancia=((ciudad_dos.cordenada_x-self.cordenada_x)**2 + (ciudad_dos.cordenada_y-self.cordenada_y)**2)**(1/2)
        return(distancia)








if __name__ == "__main__":
  x=int(input("Coordenada x: "))
  y=int(input("Coordenada y: "))
  p1=Ciudad(x,y)
  x=int(input("Coordenada x: "))
  y=int(input("Coordenada y: "))
  p2=Ciudad(x,y)
  S=p1.camino(p2)
  print(S)
  E=p1.distancia(p2)
  print(E)







         