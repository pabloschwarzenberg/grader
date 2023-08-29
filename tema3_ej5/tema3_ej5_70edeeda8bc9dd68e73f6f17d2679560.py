import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra):
        camino = [[self.x, self.y]]
        dx = otra.x - self.x
        dy = otra.y - self.y
        for i in range(1, max(abs(dx), abs(dy)) + 1):
            new_x = self.x + (i if dx > 0 else -i if dx < 0 else 0)
            new_y = self.y + (i if dy > 0 else -i if dy < 0 else 0)
            camino.append([new_x, new_y])
        return camino

    def distancia(self, otra):
        dx = otra.x - self.x
        dy = otra.y - self.y
        return math.sqrt(dx**2 + dy**2)

if __name__ == "__main__":
    p1 = Ciudad(1,1)
    p2 = Ciudad(3,3)
    print(p1.camino(p2))
    print(p1.distancia(p2))
