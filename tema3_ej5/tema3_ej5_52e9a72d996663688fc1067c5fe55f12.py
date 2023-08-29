import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        camino = []
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        pasos = max(abs(dx), abs(dy))

        if pasos == 0:
            return camino

        paso_x = dx / pasos
        paso_y = dy / pasos

        for i in range(pasos):
            punto = [round(self.x + (paso_x * i), 2), round(self.y + (paso_y * i), 2)]
            camino.append(punto)

        camino.append([otra_ciudad.x, otra_ciudad.y])
        return camino

    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        distancia = math.sqrt(dx**2 + dy**2)
        return distancia


p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)

camino_p1_p2 = p1.camino(p2)
print(camino_p1_p2)  # Resultado: [[1, 1], [2, 2], [3, 3]]

distancia_p1_p2 = p1.distancia(p2)
print(distancia_p1_p2)  # Resultado: 2.8284271247461903

