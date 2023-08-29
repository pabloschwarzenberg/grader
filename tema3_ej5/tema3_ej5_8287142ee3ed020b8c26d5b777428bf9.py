import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        x_diff = otra_ciudad.x - self.x
        y_diff = otra_ciudad.y - self.y

        pasos = max(abs(x_diff), abs(y_diff))

        camino = []
        for i in range(pasos + 1):
            x = self.x + int(i * x_diff / pasos)
            y = self.y + int(i * y_diff / pasos)
            camino.append([x, y])

        return camino

    def distancia(self, otra_ciudad):
        x_diff = otra_ciudad.x - self.x
        y_diff = otra_ciudad.y - self.y

        distancia = math.sqrt(x_diff**2 + y_diff**2)
        return distancia


p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)

camino_p1_p2 = p1.camino(p2)
print(camino_p1_p2)

distancia_p1_p2 = p1.distancia(p2)
print(distancia_p1_p2)
