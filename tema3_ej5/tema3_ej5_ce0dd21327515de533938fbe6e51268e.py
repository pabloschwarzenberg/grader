import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def camino(self, otra_ciudad):
        camino = []
        current_x = self.x
        current_y = self.y
        
        while current_x != otra_ciudad.x or current_y != otra_ciudad.y:
            camino.append([current_x, current_y])
            
            if current_x < otra_ciudad.x:
                current_x += 1
            elif current_x > otra_ciudad.x:
                current_x -= 1
                
            if current_y < otra_ciudad.y:
                current_y += 1
            elif current_y > otra_ciudad.y:
                current_y -= 1
        
        camino.append([current_x, current_y])
        return camino
    
    def distancia(self, otra_ciudad):
        delta_x = otra_ciudad.x - self.x
        delta_y = otra_ciudad.y - self.y
        distancia = math.sqrt(delta_x ** 2 + delta_y ** 2)
        return round(distancia, 2)

if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)
    
    camino = p1.camino(p2)
    print(camino)
    
    distancia = p1.distancia(p2)
    print(distancia)
