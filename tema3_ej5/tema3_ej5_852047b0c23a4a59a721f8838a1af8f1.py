import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        pasos = []
        distancia_total = 0

        # Calcula los pasos necesarios para llegar de una ciudad a otra
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        steps = max(abs(dx), abs(dy))

        if steps == 0:
            pasos.append([self.x, self.y])
            return pasos

        delta_x = dx / steps
        delta_y = dy / steps

        for i in range(steps + 1):
            x = self.x + delta_x * i
            y = self.y + delta_y * i
            pasos.append([round(x, 2), round(y, 2)])

        return pasos

    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        distancia = math.sqrt(dx ** 2 + dy ** 2)
        return distancia


if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)

    pasos = p1.camino(p2)
    print(pasos)

    distancia = p1.distancia(p2)
    print(distancia)
