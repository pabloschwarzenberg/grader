import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        pasos = []
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        distancia = max(abs(dx), abs(dy))

        for i in range(distancia + 1):
            paso_x = round(self.x + dx * (i / distancia))
            paso_y = round(self.y + dy * (i / distancia))
            pasos.append([paso_x, paso_y])

        return pasos

    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        distancia = math.sqrt(dx ** 2 + dy ** 2)
        return round(distancia, 2)


if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)
    pasos = p1.camino(p2)
    print(pasos)

    distancia = p1.distancia(p2)
    print(distancia)

         