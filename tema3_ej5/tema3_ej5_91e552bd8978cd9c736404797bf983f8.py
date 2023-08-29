import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def camino(self, otra_ciudad):
        dx, dy = otra_ciudad.x - self.x, otra_ciudad.y - self.y
        steps = max(abs(dx), abs(dy))
        return [[round(self.x + i * dx / steps), round(self.y + i * dy / steps)] for i in range(steps + 1)]
    
    def distancia(self, otra_ciudad):
        return round(math.sqrt((otra_ciudad.x - self.x)**2 + (otra_ciudad.y - self.y)**2), 2)
