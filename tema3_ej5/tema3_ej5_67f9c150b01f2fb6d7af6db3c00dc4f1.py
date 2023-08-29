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

        if steps == 0:
            return [[self.x, self.y]]

        x_step = dx / steps
        y_step = dy / steps

        for i in range(steps+1):
            x = round(self.x + i * x_step)
            y = round(self.y + i * y_step)
            camino.append([x, y])

        return camino

    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        distancia = math.sqrt(dx ** 2 + dy ** 2)
        return round(distancia, 16)


p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)

pasos = p1.camino(p2)
print(pasos)

distancia_recorrida = p1.distancia(p2)
print(distancia_recorrida)
