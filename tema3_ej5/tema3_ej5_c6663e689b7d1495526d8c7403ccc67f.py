class Ciudad:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def distancia(self,other):
        import math
        distancia=math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)
        return(distancia)
    
    def camino(self,other):
        pend=(self.y-other.y)/(self.x-other.x)
        puntos=[]
        if self.x>other.x:
            for i in range(other.x-1,self.x):
                y1=self.y+pend*((i+1)-self.x)
                x1=i+1
                puntos.append([x1,y1])
        else:
            for i in range(self.x-1,other.x):
                y1=self.y+pend*((i+1)-self.x)
                x1=i+1
                puntos.append([x1,y1])
        return(puntos)

if __name__ == "__main__":
    pass