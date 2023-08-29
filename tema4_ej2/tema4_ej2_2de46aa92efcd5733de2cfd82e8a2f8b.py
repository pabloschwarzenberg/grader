import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        pasos = []
        distancia_x = otra_ciudad.x - self.x
        distancia_y = otra_ciudad.y - self.y
        pasos_totales = max(abs(distancia_x), abs(distancia_y))

        if pasos_totales > 0:
            paso_x = distancia_x / pasos_totales
            paso_y = distancia_y / pasos_totales

            for i in range(pasos_totales + 1):
                x = round(self.x + paso_x * i)
                y = round(self.y + paso_y * i)
                pasos.append([x, y])

        return pasos

    def distancia(self, otra_ciudad):
        distancia_x = otra_ciudad.x - self.x
        distancia_y = otra_ciudad.y - self.y
        distancia = math.sqrt(distancia_x ** 2 + distancia_y ** 2)
        return round(distancia, 2)


if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)

    camino = p1.camino(p2)
    print(camino)

    distancia = p1.distancia(p2)
    print(distancia)
