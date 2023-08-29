import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        camino = []
        delta_x = otra_ciudad.x - self.x
        delta_y = otra_ciudad.y - self.y

        steps = max(abs(delta_x), abs(delta_y))
        step_x = delta_x / steps
        step_y = delta_y / steps

        for i in range(steps + 1):
            x = round(self.x + i * step_x)
            y = round(self.y + i * step_y)
            camino.append([x, y])

        return camino

    def distancia(self, otra_ciudad):
        delta_x = otra_ciudad.x - self.x
        delta_y = otra_ciudad.y - self.y
        distancia = math.sqrt(delta_x**2 + delta_y**2)
        return round(distancia, 15)  # Aumentar la precisión del redondeo

if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)

    camino = p1.camino(p2)
    print(camino)

    distancia = p1.distancia(p2)
    print(distancia)

