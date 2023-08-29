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
        paso_x = distancia_x / pasos_totales
        paso_y = distancia_y / pasos_totales

        for i in range(pasos_totales):
            x = self.x + paso_x * i
            y = self.y + paso_y * i
            pasos.append([x, y])

        pasos.append([otra_ciudad.x, otra_ciudad.y])
        return pasos
    
    def distancia(self, otra_ciudad):
        distancia_x = otra_ciudad.x - self.x
        distancia_y = otra_ciudad.y - self.y
        distancia = math.sqrt(distancia_x**2 + distancia_y**2)
        return round(distancia, 16)

