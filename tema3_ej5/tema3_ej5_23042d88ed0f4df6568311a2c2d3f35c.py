class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        pasos = [[self.x, self.y]]
        distancia_x = otra_ciudad.x - self.x
        distancia_y = otra_ciudad.y - self.y
        pasos_x = abs(distancia_x)
        pasos_y = abs(distancia_y)

        if distancia_x != 0 and distancia_y != 0:
            paso_x = distancia_x // pasos_x
            paso_y = distancia_y // pasos_y

            for i in range(1, pasos_x + 1):
                pasos.append([self.x + i * paso_x, self.y + i * paso_y])

        pasos.append([otra_ciudad.x, otra_ciudad.y])
        return pasos

    def distancia(self, otra_ciudad):
        distancia_x = otra_ciudad.x - self.x
        distancia_y = otra_ciudad.y - self.y
        distancia = (distancia_x ** 2 + distancia_y ** 2) ** 0.5
        return round(distancia, 14)


if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)
    pasos = p1.camino(p2)
    print(pasos)
    distancia = p1.distancia(p2)
    print(distancia)
