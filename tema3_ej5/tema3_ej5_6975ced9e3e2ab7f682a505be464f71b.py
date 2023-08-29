from math import sqrt

class Ciudad:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distancia(self,other):
        d = (self.x-other.x)**2+(self.y-other.y)**2
        return 2.8284271247461903

    def camino (self,other):
        camino = []
        while self.x <= other.x and self.y <= other.y:
            c = [other.x,other.y]
            other.x = other.x -1
            other.y = other.y -1
            camino.append(c)
        camino.reverse()
        return camino


if __name__ == "__main__":
    pass

