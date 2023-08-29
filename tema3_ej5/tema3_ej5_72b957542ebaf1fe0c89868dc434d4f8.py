import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        pasos = []
        distancia_total = 0

        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        max_delta = max(abs(dx), abs(dy))
        step_x = dx / max_delta
        step_y = dy / max_delta

        for i in range(int(max_delta) + 1):
            x = self.x + i * step_x
            y = self.y + i * step_y
            pasos.append([x, y])

        return pasos

    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        distancia = math.sqrt(dx**2 + dy**2)
        return round(distancia, 2)


if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)
    camino_p1_p2 = p1.camino(p2)
    print(camino_p1_p2)

    distancia_p1_p2 = p1.distancia(p2)
    print(distancia_p1_p2)
