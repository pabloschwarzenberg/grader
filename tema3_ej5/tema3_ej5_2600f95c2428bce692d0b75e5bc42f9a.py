import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        distancia_x = otra_ciudad.x - self.x
        distancia_y = otra_ciudad.y - self.y

        pasos = max(abs(distancia_x), abs(distancia_y))

        camino = []
        for i in range(pasos + 1):
            punto_x = self.x + (distancia_x // pasos) * i
            punto_y = self.y + (distancia_y // pasos) * i
            camino.append([punto_x, punto_y])

        return camino

    def distancia(self, otra_ciudad):
        distancia_x = otra_ciudad.x - self.x
        distancia_y = otra_ciudad.y - self.y
        distancia = math.sqrt(distancia_x**2 + distancia_y**2)
        return round(distancia, 2)


# Ejemplo de uso
if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)

    camino_p1_p2 = p1.camino(p2)
    print("Camino de p1 a p2:", camino_p1_p2)

    distancia_p1_p2 = p1.distancia(p2)
    print("Distancia de p1 a p2:", distancia_p1_p2)
