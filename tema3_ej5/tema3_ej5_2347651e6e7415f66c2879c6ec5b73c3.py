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
            x = round(self.x + i * paso_x)
            y = round(self.y + i * paso_y)
            camino.append([x, y])
        return camino
    
    def distancia(self, ciudad_destino):
        distancia_x = ciudad_destino.x - self.x
        distancia_y = ciudad_destino.y - self.y
        distancia = math.sqrt(distancia_x ** 2 + distancia_y ** 2)
        return distancia


if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)
    
    camino_p1_p2 = p1.camino(p2)
    print(camino_p1_p2)
    
    distancia_p1_p2 = p1.distancia(p2)
    print(distancia_p1_p2)