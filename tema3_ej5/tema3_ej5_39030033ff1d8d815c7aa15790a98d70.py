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
        step_x = dx / steps
        step_y = dy / steps
        
        for i in range(steps+1):
            x = self.x + step_x * i
            y = self.y + step_y * i
            camino.append([round(x, 9), round(y, 9)])
        
        return camino
    
    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        distancia = math.sqrt(dx**2 + dy**2)
        return round(distancia, 16)

if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)
    camino_p1_p2 = p1.camino(p2)
    distancia_p1_p2 = p1.distancia(p2)
    
    print("Camino:", camino_p1_p2)
    print("Distancia:", distancia_p1_p2)

