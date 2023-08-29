import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        pasos = []
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        distancia_total = max(abs(dx), abs(dy))

        if dx != 0 and dy != 0:
            paso_x = dx / distancia_total
            paso_y = dy / distancia_total
            for i in range(distancia_total):
                x = self.x + round(paso_x * i)
                y = self.y + round(paso_y * i)
                pasos.append([x, y])

        pasos.append([otra_ciudad.x, otra_ciudad.y])
        return pasos

    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        distancia = math.sqrt(dx ** 2 + dy ** 2)
        return round(distancia, 2)


if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)

    camino = p1.camino(p2)
    print(camino)

    distancia = p1.distancia(p2)
    print(distancia)
