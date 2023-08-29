class Ciudad:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def camino(self,other):
        lista=[]
        lista.append([self.x,self.y])
        lista.append([other.x-self.x,other.y-self.y])
        lista.append([other.x,other.y])
        return lista

    def distancia(self,other):
        a=other.x-self.x
        b=other.y-self.y
        import math
        c=math.sqrt((a**2)+(b**2))
        return c
        
if __name__ == "__main__":
    p1=Ciudad(1,1)
    p2=Ciudad(3,3)
    print(p1.distancia(p2))
    print(p1.camino(p2))