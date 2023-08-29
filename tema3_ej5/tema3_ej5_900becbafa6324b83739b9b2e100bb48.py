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
            paso_x = self.x + int(round((i / pasos) * distancia_x))
            paso_y = self.y + int(round((i / pasos) * distancia_y))
            camino.append([paso_x, paso_y])
        
        return camino
    
    def distancia(self, otra_ciudad):
        distancia_x = otra_ciudad.x - self.x
        distancia_y = otra_ciudad.y - self.y
        distancia = math.sqrt(distancia_x ** 2 + distancia_y ** 2)
        return (distancia)


p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)

camino_p1_p2 = p1.camino(p2)
print(camino_p1_p2)

distancia_p1_p2 = p1.distancia(p2)
print(distancia_p1_p2)

