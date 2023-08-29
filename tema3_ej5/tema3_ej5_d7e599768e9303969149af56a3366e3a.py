import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        dx = abs(otra_ciudad.x - self.x)
        dy = abs(otra_ciudad.y - self.y)
        steps = max(dx, dy)
        path = [[self.x, self.y]]
        for i in range(1, steps + 1):
            px = self.x + int(dx / steps * i)
            py = self.y + int(dy / steps * i)
            path.append([px, py])
        return path

    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        return math.sqrt(dx**2 + dy**2)

if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)
    camino = p1.camino(p2)
    print(camino)
    distancia = p1.distancia(p2)
    print(distancia)
