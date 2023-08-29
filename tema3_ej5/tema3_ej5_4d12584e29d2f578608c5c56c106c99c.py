import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, other):
        x1, y1 = self.x, self.y
        x2, y2 = other.x, other.y
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        steps = max(dx, dy)
        path = []
        for i in range(steps + 1):
            x = round(x1 + i * (x2 - x1) / steps)
            y = round(y1 + i * (y2 - y1) / steps)
            path.append([x, y])
        return path

    def distancia(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)

if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)
    path = p1.camino(p2)
    print(path)
    print("Distancia recorrida:", p1.distancia(p2))
         