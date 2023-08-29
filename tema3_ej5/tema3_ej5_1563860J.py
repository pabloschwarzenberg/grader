from math import sqrt
class Ciudad:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def camino(self,other):
        pasosX=abs(self.x-other.x)
        pasosY=abs(self.y-other.y)
        lista=[[self.x,self.y],[pasosX,pasosY],[other.x,other.y]]
        return lista
    def distancia(self,other):
        deltaX=self.x-other.x
        deltaY=self.y-other.y
        distancia=sqrt(deltaX**2+deltaY**2)
        return distancia


if __name__ == "__main__":
    p1=Ciudad(1,1)
    p2=Ciudad(3,3)
    b=p1.camino(p2)
    a=p1.distancia(p2)
    print(b)
    print(a)
 
         

 
         