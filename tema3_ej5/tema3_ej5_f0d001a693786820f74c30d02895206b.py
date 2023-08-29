import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        camino = []
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        steps = max(abs(dx), abs(dy))

        for i in range(steps):
            x = self.x + int(round(dx * i / steps))
            y = self.y + int(round(dy * i / steps))
            camino.append([x, y])

        camino.append([otra_ciudad.x, otra_ciudad.y])
        return camino

    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        distancia = math.sqrt(dx**2 + dy**2)
        return round(distancia, 2)

# Ejemplo de uso
p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)

camino = p1.camino(p2)
print("Camino:", camino)

distancia = p1.distancia(p2)
print("Distancia:", distancia)