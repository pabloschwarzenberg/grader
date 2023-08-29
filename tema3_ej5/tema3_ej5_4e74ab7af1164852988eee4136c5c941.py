import math

class Ciudad:
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

    def camino(self, otra_ciudad):
        ruta = []
        dx = otra_ciudad.coord_x - self.coord_x
        dy = otra_ciudad.coord_y - self.coord_y
        steps = max(abs(dx), abs(dy))
        if steps > 0:
            step_x = dx / steps
            step_y = dy / steps
            for i in range(steps + 1):
                x = self.coord_x + step_x * i
                y = self.coord_y + step_y * i
                ruta.append([x, y])
        return ruta

    def distancia(self, otra_ciudad):
        dx = otra_ciudad.coord_x - self.coord_x
        dy = otra_ciudad.coord_y - self.coord_y
        distancia = math.sqrt(dx**2 + dy**2)
        return distancia

# Ejemplo de uso:
p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)
camino = p1.camino(p2)
distancia = p1.distancia(p2)
print("Camino:", camino)
print("Distancia:", distancia)
