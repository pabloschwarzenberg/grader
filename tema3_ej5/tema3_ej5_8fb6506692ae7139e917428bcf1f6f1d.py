import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        pasos = []
        distancia_total = 0.0

        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y

        pasos.append([self.x, self.y])

        while self.x != otra_ciudad.x or self.y != otra_ciudad.y:
            if dx != 0 and dy != 0:
                step_x = math.copysign(1, dx)
                step_y = math.copysign(1, dy)
                distancia = math.sqrt(step_x ** 2 + step_y ** 2)
                distancia_total += distancia

                self.x += step_x
                self.y += step_y

                pasos.append([self.x, self.y])

                dx -= step_x
                dy -= step_y
            elif dx != 0:
                step_x = math.copysign(1, dx)
                distancia = abs(dx)
                distancia_total += distancia

                self.x += step_x

                pasos.append([self.x, self.y])

                dx -= step_x
            elif dy != 0:
                step_y = math.copysign(1, dy)
                distancia = abs(dy)
                distancia_total += distancia

                self.y += step_y

                pasos.append([self.x, self.y])

                dy -= step_y

        return pasos

    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        distancia = math.sqrt(dx ** 2 + dy ** 2)
        return round(distancia, 2)


if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)

    pasos = p1.camino(p2)
    for paso in pasos:
        print(paso)

    distancia = p1.distancia(p2)
    print("Distancia recorrida:", distancia)
