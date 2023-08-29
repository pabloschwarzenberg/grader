import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, destino):
        distancia_x = destino.x - self.x
        distancia_y = destino.y - self.y

        pasos = abs(distancia_x)
        if abs(distancia_y) > pasos:
            pasos = abs(distancia_y)

        camino = []
        for i in range(pasos + 1):
            punto_x = round(self.x + i * distancia_x / pasos)
            punto_y = round(self.y + i * distancia_y / pasos)
            camino.append([punto_x, punto_y])

        return camino

    def distancia(self, destino):
        distancia_x = destino.x - self.x
        distancia_y = destino.y - self.y
        distancia = math.sqrt(distancia_x ** 2 + distancia_y ** 2)
        return distancia

# Ejemplo de uso
p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)

camino = p1.camino(p2)
print(camino)  # [[1, 1], [2, 2], [3, 3]]

distancia = p1.distancia(p2)
print(distancia)  # 2.8284271247461903
