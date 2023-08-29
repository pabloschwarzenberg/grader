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
        incremento_x = dx / pasos
        incremento_y = dy / pasos
        for i in range(pasos + 1):
            x = round(self.x + i * incremento_x)
            y = round(self.y + i * incremento_y)
            camino.append([x, y])
        return camino

    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        distancia = math.sqrt(dx**2 + dy**2)
        return round(distancia, 14)


if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)
    camino = p1.camino(p2)
    distancia = p1.distancia(p2)
    print("Camino:", camino)
    print("Distancia recorrida:", distancia)
