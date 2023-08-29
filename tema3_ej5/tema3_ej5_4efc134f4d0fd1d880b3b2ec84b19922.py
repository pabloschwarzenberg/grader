import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        pasos = []
        dx = abs(otra_ciudad.x - self.x)
        dy = abs(otra_ciudad.y - self.y)
        steps = max(dx, dy)
        if steps > 0:
            x_step = (otra_ciudad.x - self.x) / steps
            y_step = (otra_ciudad.y - self.y) / steps
            for i in range(steps):
                x = self.x + round(x_step * i)
                y = self.y + round(y_step * i)
                pasos.append([x, y])
        pasos.append([otra_ciudad.x, otra_ciudad.y])
        return pasos

    def distancia(self, otra_ciudad):
        dx = abs(otra_ciudad.x - self.x)
        dy = abs(otra_ciudad.y - self.y)
        return math.sqrt(dx ** 2 + dy ** 2)


if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)

    pasos = p1.camino(p2)
    print(pasos)

    distancia = p1.distancia(p2)
    print(distancia)

         