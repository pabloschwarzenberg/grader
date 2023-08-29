import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        camino = []
        dx = abs(otra_ciudad.x - self.x)
        dy = abs(otra_ciudad.y - self.y)
        steps = max(dx, dy)

        if steps == 0:
            return camino

        x_step = dx / steps
        y_step = dy / steps

        for i in range(steps + 1):
            x = round(self.x + i * x_step)
            y = round(self.y + i * y_step)
            camino.append([x, y])

        return camino

    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        distancia = math.sqrt(dx**2 + dy**2)
        return round(distancia, 6)

if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)

    camino = p1.camino(p2)
    print(camino)

    distancia = p1.distancia(p2)
    print(distancia)

