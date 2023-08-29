import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        camino = []
        delta_x = otra_ciudad.x - self.x
        delta_y = otra_ciudad.y - self.y

        num_pasos = max(abs(delta_x), abs(delta_y))
        step_x = delta_x / num_pasos
        step_y = delta_y / num_pasos

        for i in range(num_pasos + 1):
            punto_x = self.x + i * step_x
            punto_y = self.y + i * step_y
            camino.append([punto_x, punto_y])

        return camino

    def distancia(self, otra_ciudad):
        delta_x = otra_ciudad.x - self.x
        delta_y = otra_ciudad.y - self.y
        distancia = math.sqrt(delta_x ** 2 + delta_y ** 2)
        return round(distancia, 2)


if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)
    camino = p1.camino(p2)
    distancia = p1.distancia(p2)

    print("Camino:", camino)
    print("Distancia:", distancia)
