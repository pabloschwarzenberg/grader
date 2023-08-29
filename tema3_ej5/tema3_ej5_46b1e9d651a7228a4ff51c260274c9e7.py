import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def camino(self, otra_ciudad):
        camino = []
        delta_x = otra_ciudad.x - self.x
        delta_y = otra_ciudad.y - self.y
        steps = max(abs(delta_x), abs(delta_y))
        
        for i in range(steps + 1):
            x = self.x + i * delta_x / steps
            y = self.y + i * delta_y / steps
            camino.append([round(x, 2), round(y, 2)])
        
        return camino
    
    def distancia(self, otra_ciudad):
        delta_x = otra_ciudad.x - self.x
        delta_y = otra_ciudad.y - self.y
        distancia = math.sqrt(delta_x ** 2 + delta_y ** 2)
        return round(distancia, 2)

if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)
    
    camino_p1_p2 = p1.camino(p2)
    print("Camino de p1 a p2:", camino_p1_p2)
    
    distancia_p1_p2 = p1.distancia(p2)
    print("Distancia de p1 a p2:", distancia_p1_p2)
