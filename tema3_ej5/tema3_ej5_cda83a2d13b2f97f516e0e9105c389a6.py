import math
class Ciudad :
    def __init__(self,x,y) :
        self.x = int(x)
        self.y = int(y)
    def __sub__(self, other) :
        x = abs(self.x - other.x)
        y = abs(self.y - other.y)
        return Ciudad(x,y)

    def distancia(self,other):
        distancia = self - other
        return math.sqrt(distancia.x ** 2 + distancia.y ** 2)
        
    def camino(self,other) :
        lista = []
        for i in range(self.distancia(other.x)) :
            lista1 = []
            lista1.append(other.x - i - 1)
            lista1.append(other.y - i - 1)
            lista.append(lista1)
        return lista

if __name__ == "__main__":
  pass
         