import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def camino(self, otra_ciudad):
        distancia_x = abs(self.x - otra_ciudad.x)
        distancia_y = abs(self.y - otra_ciudad.y)
        pasos = min(distancia_x, distancia_y) + abs(distancia_x - distancia_y)
        camino = []
        for i in range(pasos + 1):
            paso_x = self.x + (i * (otra_ciudad.x - self.x)) // pasos
            paso_y = self.y + (i * (otra_ciudad.y - self.y)) // pasos
            camino.append([paso_x, paso_y])
        return camino
    
    def distancia(self, otra_ciudad):
        distancia_x = abs(self.x - otra_ciudad.x)
        distancia_y = abs(self.y - otra_ciudad.y)
        distancia = math.sqrt(distancia_x ** 2 + distancia_y ** 2)
        return round(distancia, 14)


if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)
    camino_p1_p2 = p1.camino(p2)
    print(camino_p1_p2)
    
    distancia_p1_p2 = p1.distancia(p2)
    print(distancia_p1_p2)
