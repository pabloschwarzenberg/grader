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

        if steps == 0:
            pasos.append([self.x, self.y])
        else:
            x_step = dx / steps
            y_step = dy / steps

            for i in range(steps + 1):
                x = self.x + i * x_step
                y = self.y + i * y_step
                pasos.append([x, y])

        return pasos

    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        distancia = math.sqrt(dx**2 + dy**2)
        return distancia

if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)

    camino_p1_p2 = p1.camino(p2)
    print("Camino:", camino_p1_p2)

    distancia_p1_p2 = p1.distancia(p2)
    print("Distancia:", distancia_p1_p2)
