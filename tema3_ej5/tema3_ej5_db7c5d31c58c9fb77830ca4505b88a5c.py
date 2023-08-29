import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        ruta = []
        distancia = 0.0

        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y

        steps = max(abs(dx), abs(dy))

        if steps == 0:
            ruta.append([self.x, self.y])
        else:
            increment_x = dx / steps
            increment_y = dy / steps

            for i in range(steps + 1):
                x = round(self.x + i * increment_x)
                y = round(self.y + i * increment_y)
                ruta.append([x, y])

        for punto in ruta:
            print(punto)

        distancia = math.sqrt(dx**2 + dy**2)
        print("Distancia recorrida:", distancia)

    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
