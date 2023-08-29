import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        distancia_x = otra_ciudad.x - self.x
        distancia_y = otra_ciudad.y - self.y

        pasos_x = abs(distancia_x)
        pasos_y = abs(distancia_y)

        pasos = max(pasos_x, pasos_y)

        camino = []
        for i in range(pasos + 1):
            x = self.x + int(round(distancia_x * i / pasos))
            y = self.y + int(round(distancia_y * i / pasos))
            camino.append([x, y])

        return camino

    def distancia(self, otra_ciudad):
        distancia_x = otra_ciudad.x - self.x
        distancia_y = otra_ciudad.y - self.y
        distancia = math.sqrt(distancia_x ** 2 + distancia_y ** 2)
        return distancia


if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)

    camino_p1_p2 = p1.camino(p2)
    print("Camino de p1 a p2:", camino_p1_p2)

    distancia_p1_p2 = p1.distancia(p2)
    print("Distancia de p1 a p2:", distancia_p1_p2)
