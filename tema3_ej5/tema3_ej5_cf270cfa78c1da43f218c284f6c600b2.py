import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        pasos = []
        diferencia_x = abs(self.x - otra_ciudad.x)
        diferencia_y = abs(self.y - otra_ciudad.y)
        pasos_totales = max(diferencia_x, diferencia_y)

        for paso in range(pasos_totales + 1):
            nuevo_x = self.x + (paso * (otra_ciudad.x - self.x)) / pasos_totales
            nuevo_y = self.y + (paso * (otra_ciudad.y - self.y)) / pasos_totales
            pasos.append([round(nuevo_x), round(nuevo_y)])

        return pasos

    def distancia(self, otra_ciudad):
        diferencia_x = abs(self.x - otra_ciudad.x)
        diferencia_y = abs(self.y - otra_ciudad.y)
        distancia = math.sqrt(diferencia_x**2 + diferencia_y**2)
        return round(distancia, 2)