class Ciudad:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distancia(self,c2):
        d1=abs(c2.y-self.y)
        d2=abs(c2.x-self.x)
        d = (d1**2+d2**2)**(1/2)
        df = d
        return df
    def camino(self,c2):
        puntos =[]
        posx = self.x
        posy = self.y
        movs =[[posx,posy]]
        while (c2.y-posy)>= 1 and (c2.x-posx)>= 1:
            posx += +1
            posy += +1
            puntos.append(posx)
            puntos.append(posy)
            movs.append(puntos)
            puntos =[]
        return movs
