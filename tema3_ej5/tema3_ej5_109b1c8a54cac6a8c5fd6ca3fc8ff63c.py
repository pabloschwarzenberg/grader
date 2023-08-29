class Ciudad:
    def __init__(self,ciudadx,ciudady):
        self.ciudadx=ciudadx
        self.ciudady=ciudady
    def __eq__(self, other):
        if self.ciudadx==other.ciudadx and self.ciudady==other.ciudady:
            return True
        else:
            return False


    def camino(self,other):
        x1i=self.ciudadx
        y1i=self.ciudady
        x2i=other.ciudadx
        y2i=other.ciudady
        camino=[]
        caminox=[int(self.ciudadx)]
        caminoy=[int(self.ciudady)]
        while int(self.ciudadx) != int(other.ciudadx) and int(self.ciudady) != int(other.ciudady):
            if int(self.ciudadx)== int(other.ciudadx):
                caminox+=self.ciudadx
            if int(self.ciudadx) < int(other.ciudadx):
                caminox+=str((int(self.ciudadx)+1))
                self.ciudadx=str(int(self.ciudadx)+1)
            if int(self.ciudadx) > int(other.ciudadx):
                caminox+=str((int(self.ciudadx)-1))
                self.ciudadx=str(int(self.ciudadx)-1)
            if int(self.ciudady)== int(other.ciudady):
                caminoy+=self.ciudady
            if int(self.ciudady) < int(other.ciudady):
                caminoy+=str((int(self.ciudady)+1))
                self.ciudady=str(int(self.ciudady)+1)
            if int(self.ciudady) > int(other.ciudady):
                caminoy+=str((int(self.ciudady)-1))
                self.ciudady=str(int(self.ciudady)-1)
        for i in range(0,len(caminox)):
            x=int(caminox[i])
            y=int(caminoy[i])
            camino+=[[x,y]]
        self.ciudadx=x1i
        self.ciudady=y1i
        other.ciudadx=x2i
        other.ciudady=y2i
        return camino

    def distancia(self,other):
        x=int(self.ciudadx)-int(other.ciudadx)
        y=int(self.ciudady)-int(other.ciudady)
        distancia=(x**2+y**2)**(1/2)
        return distancia
