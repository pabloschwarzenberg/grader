import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        camino = []
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        steps = max(abs(dx), abs(dy))
        if steps > 0:
            x_step = dx / steps
            y_step = dy / steps
            for i in range(steps):
                x = self.x + x_step * i
                y = self.y + y_step * i
                camino.append([x, y])
        camino.append([otra_ciudad.x, otra_ciudad.y])
        return camino

    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        return math.sqrt(dx**2 + dy**2)


if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)
    camino = p1.camino(p2)
    print(camino)
    distancia = p1.distancia(p2)
    print(distancia)
