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
        if steps > 0:
            step_x = dx / steps
            step_y = dy / steps
            for i in range(steps):
                x = round(self.x + (i+1) * step_x)
                y = round(self.y + (i+1) * step_y)
                camino.append([x, y])
        return camino
    
    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        distancia = math.sqrt(dx**2 + dy**2)
        return round(distancia, 2)
