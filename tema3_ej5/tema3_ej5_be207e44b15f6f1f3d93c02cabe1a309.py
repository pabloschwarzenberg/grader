class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        dx = abs(self.x - otra_ciudad.x)
        dy = abs(self.y - otra_ciudad.y)
        steps = max(dx, dy)
        path = [[self.x + i * (dx // steps), self.y + i * (dy // steps)] for i in range(steps + 1)]
        return path

    def distancia(self, otra_ciudad):
        dx = abs(self.x - otra_ciudad.x)
        dy = abs(self.y - otra_ciudad.y)
        return (dx ** 2 + dy ** 2) ** 0.5

p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)

print(p1.camino(p2))
print(p1.distancia(p2))
