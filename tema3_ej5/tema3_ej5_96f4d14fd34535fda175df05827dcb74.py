import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, other):
        x1, y1 = self.x, self.y
        x2, y2 = other.x, other.y
        points = [[x1, y1]]
        while x1 != x2 or y1 != y2:
            if x1 < x2:
                x1 += 1
            elif x1 > x2:
                x1 -= 1
            if y1 < y2:
                y1 += 1
            elif y1 > y2:
                y1 -= 1
            points.append([x1, y1])
        return points

    def distancia(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)
print(p1.camino(p2))
print(p1.distancia(p2))