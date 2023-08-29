import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, ciudad_destino):
        camino = []
        distancia_x = ciudad_destino.x - self.x
        distancia_y = ciudad_destino.y - self.y
        pasos = max(abs(distancia_x), abs(distancia_y))
        paso_x = distancia_x / pasos
        paso_y = distancia_y / pasos

        for i in range(pasos + 1):
            x = self.x + paso_x * i
            y = self.y + paso_y * i
            camino.append([round(x, 2), round(y, 2)])

        return camino

    def distancia(self, ciudad_destino):
        distancia_x = ciudad_destino.x - self.x
        distancia_y = ciudad_destino.y - self.y
        distancia = math.sqrt(distancia_x**2 + distancia_y**2)
        return distancia
