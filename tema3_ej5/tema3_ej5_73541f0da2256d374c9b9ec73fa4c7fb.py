import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        distancia_x = abs(self.x - otra_ciudad.x)
        distancia_y = abs(self.y - otra_ciudad.y)
        pasos = max(distancia_x, distancia_y)
        camino = []
        for i in range(pasos + 1):
            x = self.x + i * (otra_ciudad.x - self.x) / pasos
            y = self.y + i * (otra_ciudad.y - self.y) / pasos
            camino.append([round(x, 2), round(y, 2)])
        return camino

    def distancia(self, otra_ciudad):
        distancia_x = abs(self.x - otra_ciudad.x)
        distancia_y = abs(self.y - otra_ciudad.y)
        distancia = math.sqrt(distancia_x ** 2 + distancia_y ** 2)
        return round(distancia, 17)

if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)
    camino = p1.camino(p2)
    for paso in camino:
        print(paso)
    distancia = p1.distancia(p2)
    print(distancia)
