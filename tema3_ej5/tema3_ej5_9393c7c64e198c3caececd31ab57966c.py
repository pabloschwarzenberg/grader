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

        if steps == 0:
            return pasos

        x_inc = (otra_ciudad.x - self.x) / steps
        y_inc = (otra_ciudad.y - self.y) / steps

        for i in range(steps + 1):
            x = round(self.x + x_inc * i)
            y = round(self.y + y_inc * i)
            pasos.append([x, y])

        return pasos

    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        distancia = math.sqrt(dx**2 + dy**2)
        return round(distancia, 2)


if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)
    pasos = p1.camino(p2)
    print(pasos)
    distancia = p1.distancia(p2)
    print(distancia)

         