import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        camino = []
        x1, y1 = self.x, self.y
        x2, y2 = otra_ciudad.x, otra_ciudad.y

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        steps = max(dx, dy)

        if steps == 0:
            camino.append([x1, y1])
            return camino

        x_increment = (x2 - x1) / steps
        y_increment = (y2 - y1) / steps

        for i in range(steps + 1):
            x = round(x1 + i * x_increment)
            y = round(y1 + i * y_increment)
            camino.append([x, y])

        return camino

    def distancia(self, otra_ciudad):
        x1, y1 = self.x, self.y
        x2, y2 = otra_ciudad.x, otra_ciudad.y
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return distance

# Ejemplo de uso
p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)
ruta = p1.camino(p2)
distancia = p1.distancia(p2)

print("Ruta:", ruta)
print("Distancia:", distancia)