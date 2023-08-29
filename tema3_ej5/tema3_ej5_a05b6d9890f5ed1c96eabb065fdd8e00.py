import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def camino(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        
        pasos = max(abs(dx), abs(dy))
        camino = []
        
        for i in range(pasos):
            x = self.x + int(round(dx * (i + 1) / pasos))
            y = self.y + int(round(dy * (i + 1) / pasos))
            camino.append([x, y])
        
        return camino
    
    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        
        distancia = math.sqrt(dx**2 + dy**2)
        return round(distancia, 2)

# Ejemplo de uso
p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)

ruta = p1.camino(p2)
print(ruta)  # Output: [[1, 1], [2, 2], [3, 3]]

distancia = p1.distancia(p2)
print(distancia)  # Output: 2.83

