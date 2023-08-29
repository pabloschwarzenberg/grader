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

        if distancia > 0:
            paso_x = dx / distancia
            paso_y = dy / distancia

            for i in range(distancia + 1):  # Se suma 1 para incluir la otra ciudad
                x = self.x + paso_x * i
                y = self.y + paso_y * i
                pasos.append([round(x), round(y)])

        return pasos

    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)


if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)

    camino_p1_p2 = p1.camino(p2)
    print(camino_p1_p2)

    distancia_p1_p2 = p1.distancia(p2)
    print(distancia_p1_p2)
