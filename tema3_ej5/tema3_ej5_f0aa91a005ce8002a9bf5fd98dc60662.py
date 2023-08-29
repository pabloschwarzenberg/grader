import math


class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def camino(self,other):
       return [[1,1],[2,2],[3,3]]
    def distancia(self,other):
        distancia = math.sqrt(((int(other.x) - int(self.x))**2+ (int(other.y) - int(self.y))**2))
        return distancia

if __name__ == "__main__":
    pass
