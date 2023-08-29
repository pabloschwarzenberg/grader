import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, ciudad_destino):
        distancia_x = ciudad_destino.x - self.x
        distancia_y = ciudad_destino.y - self.y
        pasos = max(abs(distancia_x), abs(distancia_y))
        camino = []
        for i in range(pasos + 1):
            x = self.x + int(distancia_x * (i / pasos))
            y = self.y + int(distancia_y * (i / pasos))
            camino.append([x, y])
        print(camino)
        return camino

    def distancia(self, ciudad_destino):
        distancia_x = ciudad_destino.x - self.x
        distancia_y = ciudad_destino.y - self.y
        distancia = math.sqrt(distancia_x ** 2 + distancia_y ** 2)
        return distancia

# Ejemplo de uso
p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)
camino = p1.camino(p2)
print(p1.distancia(p2))
