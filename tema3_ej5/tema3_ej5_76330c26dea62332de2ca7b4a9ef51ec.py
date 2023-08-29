from math import sqrt

class Ciudad:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def camino(self,city):
        d=sqrt((self.x-city.x)**2+(self.y-city.y)**2)
        return d

if __name__ == "__main__":
  p1=Ciudad(1,1)
  p2=Ciudad(3,3)
  p1.camino(p2)