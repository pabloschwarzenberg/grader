import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def camino(self, ciudad_destino):
        x_diff = ciudad_destino.x - self.x
        y_diff = ciudad_destino.y - self.y
        steps = max(abs(x_diff), abs(y_diff))
        x_step = x_diff / steps
        y_step = y_diff / steps
        camino = []
        for i in range(steps + 1):
            x = self.x + x_step * i
            y = self.y + y_step * i
            camino.append([x, y])
        return camino
    
    def distancia(self, ciudad_destino):
        x_diff = ciudad_destino.x - self.x
        y_diff = ciudad_destino.y - self.y
        distancia = math.sqrt(x_diff**2 + y_diff**2)
        return distancia

# Ejemplo de uso
p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)

camino = p1.camino(p2)
print(camino)

distancia = p1.distancia(p2)
print(distancia)