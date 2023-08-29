class Ciudad:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def camino(self,other):
        movimientos_eje_X=other.x-self.x
        movimientos_eje_Y=other.y-self.y
        return [[self.x,self.y],[movimientos_eje_X,movimientos_eje_Y],[other.x,other.y]]
    def distancia(self,other):
        distancia=((other.x-self.x)**2+(other.y-self.y)**2)**(1/2)
        return distancia
        

if __name__ == "__main__":
    p1=Ciudad(1,1)
    p2=Ciudad(3,3)
    print(p1.camino(p2))
    print(p1.distancia(p2))