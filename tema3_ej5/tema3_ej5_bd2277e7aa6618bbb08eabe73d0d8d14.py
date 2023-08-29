class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        camino = []
        diferencia_x = otra_ciudad.x - self.x
        diferencia_y = otra_ciudad.y - self.y
        pasos = max(abs(diferencia_x), abs(diferencia_y))

        incremento_x = diferencia_x / pasos
        incremento_y = diferencia_y / pasos

        for i in range(pasos + 1):
            punto_x = round(self.x + i * incremento_x, 14)
            punto_y = round(self.y + i * incremento_y, 14)
            camino.append([punto_x, punto_y])

        return camino

    def distancia(self, otra_ciudad):
        diferencia_x = otra_ciudad.x - self.x
        diferencia_y = otra_ciudad.y - self.y
        distancia = ((diferencia_x ** 2) + (diferencia_y ** 2)) ** 0.5
        return round(distancia, 14)


if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)

    lista_puntos = p1.camino(p2)
    print(lista_puntos)

    distancia_recorrida = p1.distancia(p2)
    print(distancia_recorrida)
