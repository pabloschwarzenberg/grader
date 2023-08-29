class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        camino = []
        distancia_x = abs(otra_ciudad.x - self.x)
        distancia_y = abs(otra_ciudad.y - self.y)
        pasos = max(distancia_x, distancia_y)

        paso_x = distancia_x / pasos
        paso_y = distancia_y / pasos

        for i in range(pasos + 1):
            x = round(self.x + paso_x * i)
            y = round(self.y + paso_y * i)
            camino.append([x, y])

        return camino

    def distancia(self, otra_ciudad):
        distancia_x = otra_ciudad.x - self.x
        distancia_y = otra_ciudad.y - self.y
        distancia = ((distancia_x ** 2) + (distancia_y ** 2)) ** 0.5
        return round(distancia, 15)

if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)

    camino = p1.camino(p2)
    print(camino)

    distancia = p1.distancia(p2)
    print(distancia)
