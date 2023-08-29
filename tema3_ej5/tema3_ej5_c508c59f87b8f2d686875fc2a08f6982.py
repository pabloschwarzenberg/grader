from math import sqrt
class Ciudad:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def distancia(self,other):
        d=((other.x-self.x)**2)+((other.y-self.y)**2)
        distancia=sqrt(d)
        return distancia
    def camino(self,other):
        x=abs(self.x-other.x)
        y=abs(self.y-other.y)
        
if __name__ == "__main__":
  pass
         