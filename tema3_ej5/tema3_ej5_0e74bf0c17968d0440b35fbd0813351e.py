import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        pasos = []
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        steps = max(abs(dx), abs(dy))
        if steps > 0:
            x_step = dx / steps
            y_step = dy / steps
            for i in range(steps + 1):
                x = round(self.x + x_step * i)
                y = round(self.y + y_step * i)
                pasos.append([x, y])
        return pasos

    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)

if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)
    pasos = p1.camino(p2)
    print(pasos)
    distancia = p1.distancia(p2)
    print(distancia)


         