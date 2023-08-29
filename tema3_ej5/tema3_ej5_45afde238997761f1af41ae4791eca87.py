import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        pasos = []
        distancia_total = self.distancia(otra_ciudad)

        num_pasos = max(abs(otra_ciudad.x - self.x), abs(otra_ciudad.y - self.y))

        if num_pasos == 0:
            return []

        x_step = (otra_ciudad.x - self.x) / num_pasos
        y_step = (otra_ciudad.y - self.y) / num_pasos

        for i in range(num_pasos):
            x = self.x + x_step * i
            y = self.y + y_step * i
            pasos.append([x, y])

        pasos.append([otra_ciudad.x, otra_ciudad.y])

        return pasos

    def distancia(self, otra_ciudad):
        distancia = math.sqrt((otra_ciudad.x - self.x) ** 2 + (otra_ciudad.y - self.y) ** 2)
        return round(distancia, 8)


if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)

    pasos = p1.camino(p2)
    print("Pasos:", pasos)

    distancia = p1.distancia(p2)
    print("Distancia:", distancia)
