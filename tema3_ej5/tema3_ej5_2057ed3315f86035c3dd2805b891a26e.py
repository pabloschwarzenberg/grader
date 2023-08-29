class Ciudad:
  pass

if __name__ == "__main__":
  pass
import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, other):
        pasos = []
        dx = other.x - self.x
        dy = other.y - self.y
        steps = max(abs(dx), abs(dy))
        if steps > 0:
            x_step = dx / steps
            y_step = dy / steps
            for i in range(steps):
                x = self.x + x_step * (i + 1)
                y = self.y + y_step * (i + 1)
                pasos.append([x, y])
        return pasos

    def distancia(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        distancia = math.sqrt(dx ** 2 + dy ** 2)
        return round(distancia, 2)


if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)
    pasos = p1.camino(p2)
    print(pasos)
    distancia = p1.distancia(p2)
    print(distancia)
