import math
class Ciudad:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def camino(self,other):
        self.ciudad_1 = [self.x,self.y]
        self.ciudad_2 = [other.x,other.y]
        pasos = [abs(int(self.x-other.x)),abs(int(other.y-self.y))]
        return [self.ciudad_1,pasos,self.ciudad_2]
    def distancia(self,other):
        distancia_x = (self.x-other.x)*(self.x-other.x)
        distancia_y = (self.y-other.y)*(self.y-other.y)
        distancia = math.sqrt(float(distancia_x+distancia_y))
        return distancia