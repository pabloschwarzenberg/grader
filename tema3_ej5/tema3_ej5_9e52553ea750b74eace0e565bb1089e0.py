import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        x_diff = otra_ciudad.x - self.x
        y_diff = otra_ciudad.y - self.y

        steps = max(abs(x_diff), abs(y_diff))
        x_step = x_diff / steps
        y_step = y_diff / steps

        path = []
        for i in range(steps):
            x = self.x + x_step * i
            y = self.y + y_step * i
            path.append([x, y])

        return path

    def distancia(self, otra_ciudad):
        x_diff = otra_ciudad.x - self.x
        y_diff = otra_ciudad.y - self.y

        distance = math.sqrt(x_diff**2 + y_diff**2)
        return round(distance, 2)


if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)

    camino_p1_p2 = p1.camino(p2)
    print("Camino:", camino_p1_p2)

    distancia_p1_p2 = p1.distancia(p2)
    print("Distancia:", distancia_p1_p2)


        camino = []
        for i in range(steps):
            x = round(self.x + (i * x_step))
            y = round(self.y + (i * y_step))
            camino.append([x, y])

        print(camino)

    def distancia(self, otra_ciudad):
        x_diff = otra_ciudad.x - self.x
        y_diff = otra_ciudad.y - self.y

        distance = math.sqrt(x_diff**2 + y_diff**2)
        return round(distance, 2)

if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)

    p1.camino(p2)
    print(p1.distancia(p2))
