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
            return camino

        x_step = dx / steps
        y_step = dy / steps

        for i in range(steps):
            x = round(self.x + (x_step * i))
            y = round(self.y + (y_step * i))
            camino.append([x, y])

        camino.append([otra_ciudad.x, otra_ciudad.y])
        return camino

    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        distancia = math.sqrt(dx**2 + dy**2)
        return distancia
