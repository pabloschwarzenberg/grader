import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, ciudad_destino):
        dx = ciudad_destino.x - self.x
        dy = ciudad_destino.y - self.y
        distancia = max(abs(dx), abs(dy))
        pasos = []
        for i in range(distancia + 1):
            x = self.x + int(i * dx / distancia)
            y = self.y + int(i * dy / distancia)
            pasos.append([x, y])
        return pasos

    def distancia(self, ciudad_destino):
        dx = ciudad_destino.x - self.x
        dy = ciudad_destino.y - self.y
        return math.sqrt(dx**2 + dy**2)

if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)
    camino = p1.camino(p2)
    distancia = p1.distancia(p2)
    print(camino)
    print(distancia)         