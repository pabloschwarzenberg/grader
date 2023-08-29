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
        if dx == 0:
            for i in range(y1, y2 + 1):
                pasos.append([x1, i])
        elif dy == 0:
            for i in range(x1, x2 + 1):
                pasos.append([i, y1])
        else:
            m = dy / dx
            b = y1 - m * x1
            if abs(dx) > abs(dy):
                for i in range(x1, x2 + 1):
                    y = m * i + b
                    pasos.append([i, round(y)])
            else:
                for i in range(y1, y2 + 1):
                    x = (i - b) / m
                    pasos.append([round(x), i])
        return pasos

    def distancia(self, otra_ciudad):
        x1, y1 = self.x, self.y
        x2, y2 = otra_ciudad.x, otra_ciudad.y
        return math.sqrt((x2 - x1) * 2 + (y2 - y1) * 2)

p1 = Ciudad(1,1)
p2 = Ciudad(3,3)
print(p1.camino(p2))
print(p1.distancia(p2))