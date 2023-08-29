class Ciudad:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def distancia(self,other):
        distancia=((self.x-other.x)**2+(self.y-other.y)**2)**(1/2)
        return distancia

    def camino(self,other):
        camino=[]
        camino.append([self.x,self.y])
        i=1
        while i<abs(self.x-other.x):
            camino.append([self.x+i,self.y+i])
            i+=1
        camino.append([other.x,other.y])
        return camino
        
if __name__ == "__main__":
  pass