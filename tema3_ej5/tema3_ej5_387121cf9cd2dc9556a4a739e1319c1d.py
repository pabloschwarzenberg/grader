import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        x1, y1 = self.x, self.y
        x2, y2 = otra_ciudad.x, otra_ciudad.y

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        steps = max(dx, dy)

        path = []
        for step in range(steps + 1):
            x = x1 + (step * dx) / steps
            y = y1 + (step * dy) / steps
            path.append([x, y])

        return path

    def distancia(self, otra_ciudad):
        x1, y1 = self.x, self.y
        x2, y2 = otra_ciudad.x, otra_ciudad.y

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        return math.sqrt(dx ** 2 + dy ** 2)

if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)

    camino_p1_p2 = p1.camino(p2)
    distancia_p1_p2 = p1.distancia(p2)

    print("Camino de p1 a p2:")
    print(camino_p1_p2)
    print("Distancia entre p1 y p2:", distancia_p1_p2)
         