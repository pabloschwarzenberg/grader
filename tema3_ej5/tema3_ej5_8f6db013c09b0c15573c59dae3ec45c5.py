import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        pasos = []
        diff_x = otra_ciudad.x - self.x
        diff_y = otra_ciudad.y - self.y
        num_pasos = max(abs(diff_x), abs(diff_y))
        step_x = diff_x / num_pasos
        step_y = diff_y / num_pasos

        for i in range(num_pasos):
            x = round(self.x + i * step_x)
            y = round(self.y + i * step_y)
            pasos.append([x, y])

        pasos.append([otra_ciudad.x, otra_ciudad.y])
        return pasos

    def distancia(self, otra_ciudad):
        diff_x = otra_ciudad.x - self.x
        diff_y = otra_ciudad.y - self.y
        distancia = math.sqrt(diff_x**2 + diff_y**2)
        return distancia

if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)
    pasos = p1.camino(p2)
    print(pasos)
    distancia = p1.distancia(p2)
    print(round(distancia, 2))
         