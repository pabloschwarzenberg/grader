import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def camino(self, otra_ciudad):
        camino = []
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        steps = max(abs(dx), abs(dy))
        
        for i in range(steps):
            x_step = self.x + int((dx / steps) * i)
            y_step = self.y + int((dy / steps) * i)
            camino.append([x_step, y_step])
        
        camino.append([otra_ciudad.x, otra_ciudad.y])
        return camino
    
    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        distancia = math.sqrt(dx ** 2 + dy ** 2)
        return distancia

# Ejemplo de uso
p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)

camino = p1.camino(p2)
print(camino)

distancia = p1.distancia(p2)
print(distancia)
