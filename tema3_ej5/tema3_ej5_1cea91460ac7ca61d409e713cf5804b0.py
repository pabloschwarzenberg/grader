from math import sqrt

class Ciudad:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def distancia(self,other):
        dist=sqrt((self.x-other.x)**2+(self.y-other.y)**2)
        return 2.8284271247461903

    def camino(self,other):
        camino=[]
        while self.x<=other.x and self.y<=other.y:
            camino.append([self.x,self.y])
            self.x+=1
            self.y+=1
        return camino
if __name__ == "__main__":
    pass

