import math
class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        pasos = []
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        paso_x = 1 if dx > 0 else -1
        paso_y = 1 if dy > 0 else -1

        while self.x != otra_ciudad.x or self.y != otra_ciudad.y:
            pasos.append([self.x, self.y])
            self.x += paso_x
            self.y += paso_y

        pasos.append([self.x, self.y])
        return pasos

    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        distancia = math.sqrt(dx**2 + dy**2)
        return round(distancia, 2)


if __name__ == "__main__":
    p1 = Ciudad(1,1)
    p2 = Ciudad(3,3)

    camino_p1_p2 = p1.camino(p2)
    print(camino_p1_p2)

    distancia_p1_p2 = p1.distancia(p2)
    print(distancia_p1_p2)
         