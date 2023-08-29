import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def camino(self, otra_ciudad):
        x1, y1 = self.x, self.y
        x2, y2 = otra_ciudad.x, otra_ciudad.y
        
        distancia_x = abs(x2 - x1)
        distancia_y = abs(y2 - y1)
        distancia = max(distancia_x, distancia_y)
        
        pasos = []
        paso_x = 1 if x2 > x1 else -1
        paso_y = 1 if y2 > y1 else -1
        
        for i in range(distancia + 1):
            x = x1 + paso_x * i
            y = y1 + paso_y * i
            pasos.append([x, y])
        
        return pasos
    
    def distancia(self, otra_ciudad):
        x1, y1 = self.x, self.y
        x2, y2 = otra_ciudad.x, otra_ciudad.y
        
        distancia_x = abs(x2 - x1)
        distancia_y = abs(y2 - y1)
        
        distancia = math.sqrt(distancia_x ** 2 + distancia_y ** 2)
        return distancia

p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)

camino = p1.camino(p2)
print(camino)

distancia = p1.distancia(p2)
print(distancia)