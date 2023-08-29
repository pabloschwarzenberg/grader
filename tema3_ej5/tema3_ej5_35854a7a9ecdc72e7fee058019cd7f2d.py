import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        pasos = []
        diff_x = otra_ciudad.x - self.x
        diff_y = otra_ciudad.y - self.y

        signo_x = 1 if diff_x > 0 else -1
        signo_y = 1 if diff_y > 0 else -1

        diff_x = abs(diff_x)
        diff_y = abs(diff_y)

        incremento = max(diff_x, diff_y)
        ratio_x = diff_x / incremento
        ratio_y = diff_y / incremento

        for i in range(incremento + 1):
            x = self.x + signo_x * round(ratio_x * i)
            y = self.y + signo_y * round(ratio_y * i)
            pasos.append([x, y])

        return pasos

    def distancia(self, otra_ciudad):
        diff_x = otra_ciudad.x - self.x
        diff_y = otra_ciudad.y - self.y
        distancia = math.sqrt(diff_x ** 2 + diff_y ** 2)
        return round(distancia, 16)