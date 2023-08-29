import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        pasos = []
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        distancia = max(abs(dx), abs(dy))

        if distancia > 0:
            step_x = dx / distancia
            step_y = dy / distancia

            for i in range(distancia + 1):
                x = round(self.x + step_x * i)
                y = round(self.y + step_y * i)
                pasos.append([x, y])

        return pasos

    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        distancia = math.sqrt(dx**2 + dy**2)
        return round(distancia, 15)


if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)

    pasos = p1.camino(p2)
    print(pasos)  # [[1, 1], [2, 2], [3, 3]]

    distancia = p1.distancia(p2)
    print(distancia)  # 2.8284271247461903
