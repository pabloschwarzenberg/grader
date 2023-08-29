import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def camino(self, otra_ciudad):
        distancia_x = otra_ciudad.x - self.x
        distancia_y = otra_ciudad.y - self.y
        pasos = abs(distancia_x) + abs(distancia_y)
        direccion_x = 1 if distancia_x > 0 else -1
        direccion_y = 1 if distancia_y > 0 else -1
        camino = []
        for i in range(pasos):
            punto_x = self.x + (i * direccion_x)
            punto_y = self.y + (i * direccion_y)
            camino.append([punto_x, punto_y])
        return camino
    
    def distancia(self, otra_ciudad):
        distancia_x = otra_ciudad.x - self.x
        distancia_y = otra_ciudad.y - self.y
        distancia = math.sqrt(distancia_x**2 + distancia_y**2)
        return round(distancia, 2)



