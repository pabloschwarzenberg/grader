import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        pasos = []
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        max_steps = max(abs(dx), abs(dy))

        if max_steps == 0:
            return pasos

        step_x = dx / max_steps
        step_y = dy / max_steps

        for i in range(max_steps):
            x = self.x + round(step_x * i)
            y = self.y + round(step_y * i)
            pasos.append([x, y])

        pasos.append([otra_ciudad.x, otra_ciudad.y])
        return pasos

    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)
p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)

pasos = p1.camino(p2)
print("Pasos:", pasos)

distancia = p1.distancia(p2)
print("Distancia:", round(distancia, 2))

