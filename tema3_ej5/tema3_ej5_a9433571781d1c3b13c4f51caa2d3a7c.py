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
        
        if pasos == 0:
            return camino
        
        paso_x = distancia_x / pasos
        paso_y = distancia_y / pasos
        
        for i in range(pasos):
            x = self.x + int(paso_x * i)
            y = self.y + int(paso_y * i)
            camino.append([x, y])
        
        camino.append([otra_ciudad.x, otra_ciudad.y])
        return camino
    
    def distancia(self, otra_ciudad):
        distancia_x = otra_ciudad.x - self.x
        distancia_y = otra_ciudad.y - self.y
        distancia = math.sqrt(distancia_x ** 2 + distancia_y ** 2)
        return round(distancia, 2)


p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)

camino_p1_p2 = p1.camino(p2)
distancia_p1_p2 = p1.distancia(p2)

print("Camino:", camino_p1_p2)
print("Distancia:", distancia_p1_p2)