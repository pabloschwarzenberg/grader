import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, destino):
        camino = []
        dx = destino.x - self.x
        dy = destino.y - self.y
        steps = max(abs(dx), abs(dy))

        if steps > 0:
            x_step = dx / steps
            y_step = dy / steps

            for i in range(steps):
                x = self.x + x_step * i
                y = self.y + y_step * i
                camino.append([x, y])

        camino.append([destino.x, destino.y])
        return camino

    def distancia(self, destino):
        dx = destino.x - self.x
        dy = destino.y - self.y
        return math.sqrt(dx**2 + dy**2)


if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)

    camino_p1_p2 = p1.camino(p2)
    print(camino_p1_p2)

    distancia_p1_p2 = p1.distancia(p2)
    print(distancia_p1_p2)
   