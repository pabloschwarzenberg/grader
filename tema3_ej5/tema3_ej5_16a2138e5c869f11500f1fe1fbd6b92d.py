import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def camino(self, otra_ciudad):
        pasos = []
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        steps = max(abs(dx), abs(dy))
        x_step = dx / steps
        y_step = dy / steps
        
        for i in range(steps):
            x = self.x + round(x_step * i)
            y = self.y + round(y_step * i)
            pasos.append([x, y])
        
        pasos.append([otra_ciudad.x, otra_ciudad.y])
        return pasos
    
    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        distancia = math.sqrt(dx**2 + dy**2)
        return round(distancia, 2)
