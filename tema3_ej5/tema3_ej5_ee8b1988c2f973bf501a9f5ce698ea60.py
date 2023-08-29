import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, ciudad_destino):
        pasos = []
        dx = ciudad_destino.x - self.x
        dy = ciudad_destino.y - self.y
        steps = max(abs(dx), abs(dy))
        if steps == 0:
            return pasos
        x_inc = dx / steps
        y_inc = dy / steps
        for i in range(steps):
            x = round(self.x + i * x_inc)
            y = round(self.y + i * y_inc)
            pasos.append([x, y])
        pasos.append([ciudad_destino.x, ciudad_destino.y])
        return pasos

    def distancia(self, ciudad_destino):
        dx = ciudad_destino.x - self.x
        dy = ciudad_destino.y - self.y
        distancia = math.sqrt(dx**2 + dy**2)
        return distancia

if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)
    camino = p1.camino(p2)
    print(camino)
    distancia = p1.distancia(p2)
    print(distancia)
