import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        camino = []
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        steps = max(abs(dx), abs(dy))

        if steps == 0:
            return []

        x_step = dx / steps
        y_step = dy / steps

        for i in range(steps):
            self.x += x_step
            self.y += y_step
            camino.append([round(self.x), round(self.y)])

        return camino

    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        distancia = math.sqrt(dx**2 + dy**2)
        return round(distancia, 9)


# Ejemplo de uso
p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)

pasos = p1.camino(p2)
print("Camino:", pasos)

distancia = p1.distancia(p2)
print("Distancia:", distancia)
