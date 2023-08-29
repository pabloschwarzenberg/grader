import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, other):
        camino = [[self.x, self.y], [other.x, other.y]]
        return camino

    def distancia(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        distancia = math.sqrt(dx**2 + dy**2)
        return round(distancia, 16)


if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)
    camino = p1.camino(p2)
    print("Camino:", camino)
    distancia = p1.distancia(p2)
    print("Distancia:", distancia)


         