import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        pasos = []
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        x = self.x
        y = self.y

        while x != otra_ciudad.x or y != otra_ciudad.y:
            if dx > 0:
                x += 1
                dx -= 1
            elif dx < 0:
                x -= 1
                dx += 1

            if dy > 0:
                y += 1
                dy -= 1
            elif dy < 0:
                y -= 1
                dy += 1

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
    print("Pasos:", pasos)

    distancia = p1.distancia(p2)
    print("Distancia:", distancia)
