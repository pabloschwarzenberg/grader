class Ciudad:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.lista_1=[]
    def camino(self,other):
        self.lista_1.append([self.x,self.y])
        self.lista_1.append([other.x-self.x,other.y-self.y])
        self.lista_1.append([other.x,other.y])
        return self.lista_1
    def distancia(self,other):
        return ((self.x-other.x)**2+(self.y-other.y)**2)**(1/2)