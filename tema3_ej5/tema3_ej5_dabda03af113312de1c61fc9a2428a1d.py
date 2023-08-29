import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, ciudad_destino):
        camino = []
        distancia = max(abs(ciudad_destino.x - self.x), abs(ciudad_destino.y - self.y))

        dx = (ciudad_destino.x - self.x) / distancia
        dy = (ciudad_destino.y - self.y) / distancia

        x = self.x
        y = self.y

        for _ in range(int(distancia)):
            x += dx
            y += dy
            camino.append([round(x), round(y)])

        return camino

    def distancia(self, ciudad_destino):
        dx = ciudad_destino.x - self.x
        dy = ciudad_destino.y - self.y
        distancia = math.sqrt(dx**2 + dy**2)
        return round(distancia, 2)
