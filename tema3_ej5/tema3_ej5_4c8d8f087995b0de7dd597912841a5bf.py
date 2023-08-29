import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, ciudad_destino):
        camino = []
        dx = ciudad_destino.x - self.x
        dy = ciudad_destino.y - self.y
        steps = max(abs(dx), abs(dy))

        for i in range(steps):
            x = self.x + dx * i / steps
            y = self.y + dy * i / steps
            camino.append([x, y])

        camino.append([ciudad_destino.x, ciudad_destino.y])
        return camino

    def distancia(self, ciudad_destino):
        dx = ciudad_destino.x - self.x
        dy = ciudad_destino.y - self.y
        distancia = math.sqrt(dx**2 + dy**2)
        return distancia

if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)
    camino = p1.camino(p2)
    print(camino)
    distancia = p1.distancia(p2)
    print(distancia)
