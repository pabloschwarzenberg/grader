class Ciudad:
  pass

if __name__ == "__main__":
  pass
import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        distancia_x = otra_ciudad.x - self.x
        distancia_y = otra_ciudad.y - self.y

        pasos = abs(distancia_x)
        if abs(distancia_y) > pasos:
            pasos = abs(distancia_y)

        camino = []
        for i in range(pasos + 1):
            x = self.x + (distancia_x * i // pasos)
            y = self.y + (distancia_y * i // pasos)
            camino.append([x, y])

        return camino

    def distancia(self, otra_ciudad):
        distancia_x = otra_ciudad.x - self.x
        distancia_y = otra_ciudad.y - self.y

        distancia = math.sqrt(distancia_x**2 + distancia_y**2)
        return round(distancia, 2)


if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)

    camino = p1.camino(p2)
    print(camino)

    distancia = p1.distancia(p2)
    print(distancia)
         