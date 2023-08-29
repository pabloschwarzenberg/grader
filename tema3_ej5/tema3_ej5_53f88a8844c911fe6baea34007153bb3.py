class Ciudad:
    def __init__(self,x,y):
      self.x=int(x)
      self.y=int(y)

    def distancia(self,other):
        distanciaX=other.x-self.x
        distanciaY=other.y-self.y
        distancia=((distanciaX)**2+(distanciaY)**2)**(1/2)
        return distancia

    def camino(self,other):
        cambioX=(other.x-self.x)/5
        cambioY=(other.y-self.y)/5
        pasos=[]
        for i in range(6):
            pasos.append([self.x+cambioX*i,self.y+cambioY*i])
        return pasos
        

if __name__ == "__main__":
    x1,y1=input("Ingresa coordenadas de la primera ciudad: ").split(",")
    x2,y2=input("Ingresa coordenadas de la segunda ciudad: ").split(",")
    p1=Ciudad(x1,y1)
    p2=Ciudad(x2,y2)
    print(p1.camino(p2))
    print(p1.distancia(p2))