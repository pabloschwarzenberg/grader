import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def camino(self, destino):
        camino = []
        x_diff = destino.x - self.x
        y_diff = destino.y - self.y
        x_step = 1 if x_diff > 0 else -1
        y_step = 1 if y_diff > 0 else -1

        while self.x != destino.x or self.y != destino.y:
            camino.append([self.x, self.y])
            self.x += x_step
            self.y += y_step

        camino.append([destino.x, destino.y])
        return camino
    
    def distancia(self, destino):
        x_diff = destino.x - self.x
        y_diff = destino.y - self.y
        distancia = math.sqrt(x_diff ** 2 + y_diff ** 2)
        return round(distancia, 2)

# Ejemplo de uso
p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)

camino = p1.camino(p2)
print(camino)

distancia = p1.distancia(p2)
print(distancia)
