import math


class Ciudad:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def camino(self, other):
        kepler = [self.x, self.y]
        bruno = [other.x, other.y]
        newton = [(self.x - other.x), (self.y - other.x)]
        lista = [kepler, newton,bruno]
        return lista

    def distancia(self, other):
        distancia=math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        return distancia


if __name__ == "__main__":
  p1 = Ciudad(1, 1)
  p2 = Ciudad(3, 3)
  p1.distancia(p2)
