import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        pasos = []
        distancia_x = otra_ciudad.x - self.x
        distancia_y = otra_ciudad.y - self.y
        pasos_totales = max(abs(distancia_x), abs(distancia_y))

        if pasos_totales > 0:
            paso_x = distancia_x / pasos_totales
            paso_y = distancia_y / pasos_totales

            for i in range(pasos_totales + 1):
                paso_actual_x = round(self.x + i * paso_x)
                paso_actual_y = round(self.y + i * paso_y)
                pasos.append([paso_actual_x, paso_actual_y])

        return pasos

    def distancia(self, otra_ciudad):
        distancia_x = otra_ciudad.x - self.x
        distancia_y = otra_ciudad.y - self.y
        distancia = math.sqrt(distancia_x**2 + distancia_y**2)
        return round(distancia, 2)


if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)

    lista_pasos = p1.camino(p2)
    print(lista_pasos)

    distancia_recorrida = p1.distancia(p2)
    print(distancia_recorrida