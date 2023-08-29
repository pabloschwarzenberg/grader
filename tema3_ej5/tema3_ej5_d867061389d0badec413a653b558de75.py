from math import sqrt
class Ciudad:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def camino(self,otro):
        puntos=[]
        puntos.append(Ciudad(otro.x,otro.y))
        for punto in puntos:
            print(punto)
    def distancia(self,otro):
        dx=(self.x-otro.x)**2
        dy=(self.y-otro.y)**2
        print(sqrt(dx+dy))
    pass

if __name__ == "__main__":
    pass         