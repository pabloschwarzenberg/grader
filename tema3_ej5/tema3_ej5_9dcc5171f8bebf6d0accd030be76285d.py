import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def camino(self, ciudad_destino):
        current_x = self.x
        current_y = self.y
        camino = [(current_x, current_y)]
        
        while current_x != ciudad_destino.x or current_y != ciudad_destino.y:
            if current_x < ciudad_destino.x:
                current_x += 1
            elif current_x > ciudad_destino.x:
                current_x -= 1
            
            if current_y < ciudad_destino.y:
                current_y += 1
            elif current_y > ciudad_destino.y:
                current_y -= 1
            
            camino.append((current_x, current_y))
        
        return camino
    
    def distancia(self, ciudad_destino):
        dx = ciudad_destino.x - self.x
        dy = ciudad_destino.y - self.y
        distancia = math.sqrt(dx ** 2 + dy ** 2)
        return distancia

if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)
    print("Pasos del camino:")
    camino = p1.camino(p2)
    for paso in camino:
        print(paso)
    print("Distancia recorrida:")
    print(p1.distancia(p2))
