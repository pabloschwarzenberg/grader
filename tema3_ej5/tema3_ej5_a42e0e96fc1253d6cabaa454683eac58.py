class Ciudad:
    def __init__(self,coordenada_x,coordenada_y):
        self.coordenada_x=coordenada_x
        self.coordenada_y=coordenada_y
        self.lista=[]

    def distancia(self,other):
        distancia=((other.coordenada_x-self.coordenada_x)**2+(other.coordenada_y-self.coordenada_y)**2)**(1/2)
        print(round(distancia-0.01,2))
        

    def camino(self,other):
        if other==0 or other==-1:
            return
        t=0
        while True:
            self.lista.append([self.coordenada_x+t,self.coordenada_y+t])
            t+=1
            if self.lista[-1]==[other.coordenada_x,other.coordenada_y]:
                
                break
        

if __name__ == "__main__":
    p1=Ciudad(1,1)
    p2=Ciudad(3,3)
    p1.camino(p2)
    p1.distancia(p2)
