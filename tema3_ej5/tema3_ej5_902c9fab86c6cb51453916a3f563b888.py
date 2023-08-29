import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        camino = []
        delta_x = abs(otra_ciudad.x - self.x)
        delta_y = abs(otra_ciudad.y - self.y)
        pasos = max(delta_x, delta_y)

        if pasos == 0:
            return []

        step_x = (otra_ciudad.x - self.x) / pasos
        step_y = (otra_ciudad.y - self.y) / pasos

        for i in range(pasos + 1):
            punto_x = round(self.x + i * step_x)
            punto_y = round(self.y + i * step_y)
            camino.append([punto_x, punto_y])

        return camino

    def distancia(self, otra_ciudad):
        delta_x = otra_ciudad.x - self.x
        delta_y = otra_ciudad.y - self.y
        distancia = math.sqrt(delta_x ** 2 + delta_y ** 2)
        return round(distancia, 2)


# Ejemplo de uso
p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)

# Obtener el camino entre p1 y p2
camino_p1_p2 = p1.camino(p2)
print("Camino:", camino_p1_p2)

# Calcular la distancia entre p1 y p2
distancia_p1_p2 = p1.distancia(p2)
print("Distancia:", distancia_p1_p2)