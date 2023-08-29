import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def camino(self, otra_ciudad):
        distancia_x = otra_ciudad.x - self.x
        distancia_y = otra_ciudad.y - self.y
        
        pasos_x = abs(distancia_x)
        pasos_y = abs(distancia_y)
        
        direccion_x = 1 if distancia_x > 0 else -1
        direccion_y = 1 if distancia_y > 0 else -1
        
        pasos_totales = max(pasos_x, pasos_y)
        camino = []
        
        for paso in range(pasos_totales):
            nuevo_x = self.x + direccion_x * paso
            nuevo_y = self.y + direccion_y * paso
            camino.append([nuevo_x, nuevo_y])
        
        camino.append([otra_ciudad.x, otra_ciudad.y])
        
        return camino
    
    def distancia(self, otra_ciudad):
        distancia_x = otra_ciudad.x - self.x
        distancia_y = otra_ciudad.y - self.y
        
        distancia = math.sqrt(distancia_x**2 + distancia_y**2)
        return round(distancia, 14)

if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)
    camino = p1.camino(p2)
    distancia = p1.distancia(p2)
    
    print("Camino:", camino)
    print("Distancia:", distancia)