import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        camino = []
        diferencia_x = otra_ciudad.x - self.x
        diferencia_y = otra_ciudad.y - self.y
        pasos = max(abs(diferencia_x), abs(diferencia_y))
        paso_x = diferencia_x / pasos
        paso_y = diferencia_y / pasos
        for i in range(pasos + 1):
            x = self.x + i * paso_x
            y = self.y + i * paso_y
            camino.append([x, y])
        return camino

    def distancia(self, otra_ciudad):
        diferencia_x = otra_ciudad.x - self.x
        diferencia_y = otra_ciudad.y - self.y
        distancia = math.sqrt(diferencia_x ** 2 + diferencia_y ** 2)
        return distancia


# Ejemplo de uso
p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)

camino_p1_p2 = p1.camino(p2)
print("Camino:", camino_p1_p2)

distancia_p1_p2 = p1.distancia(p2)
print("Distancia:", distancia_p1_p2)
