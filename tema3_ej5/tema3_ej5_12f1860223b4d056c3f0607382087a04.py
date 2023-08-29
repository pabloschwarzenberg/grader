import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        x1, y1 = self.x, self.y
        x2, y2 = otra_ciudad.x, otra_ciudad.y
        dx = x2 - x1
        dy = y2 - y1
        pasos = []
        for i in range(abs(dx) + 1):
            x = x1 + i if dx >= 0 else x1 - i
            y = int(round(y1 + dy * i / abs(dx))) if dx != 0 else y1
            pasos.append([x, y])
        return pasos

    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        return math.sqrt(dx**2 + dy**2)
