import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        x_actual = self.x
        y_actual = self.y
        pasos = []

        while x_actual != otra_ciudad.x or y_actual != otra_ciudad.y:
            if x_actual < otra_ciudad.x:
                x_actual += 1
            elif x_actual > otra_ciudad.x:
                x_actual -= 1

            if y_actual < otra_ciudad.y:
                y_actual += 1
            elif y_actual > otra_ciudad.y:
                y_actual -= 1

            pasos.append([x_actual, y_actual])

        return pasos

    def distancia(self, otra_ciudad):
        distancia_x = abs(self.x - otra_ciudad.x)
        distancia_y = abs(self.y - otra_ciudad.y)
        distancia = math.sqrt(distancia_x**2 + distancia_y**2)
        return round(distancia, 2)


if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)

    pasos = p1.camino(p2)
    print(pasos)

    distancia = p1.distancia(p2)
    print(distancia)
