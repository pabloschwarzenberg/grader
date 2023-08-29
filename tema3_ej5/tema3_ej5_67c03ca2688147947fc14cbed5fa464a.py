import math
class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        x1 = self.x
        y1 = self.y
        x2 = otra_ciudad.x
        y2 = otra_ciudad.y
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        steps = max(dx, dy)
        path = []
        for i in range(steps + 1):
            x = x1 + i * (x2 - x1) / steps
            y = y1 + i * (y2 - y1) / steps
            path.append([x, y])
        return path

    def distancia(self, otra_ciudad):
        x1 = self.x
        y1 = self.y
        x2 = otra_ciudad.x
        y2 = otra_ciudad.y
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        return math.sqrt(dx * dx + dy * dy)