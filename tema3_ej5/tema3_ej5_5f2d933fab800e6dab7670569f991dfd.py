import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def camino(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        distancia = max(abs(dx), abs(dy))
        pasos = []
        for i in range(distancia + 1):
            x = self.x + int(round(i * dx / distancia))
            y = self.y + int(round(i * dy / distancia))
            pasos.append([x, y])
        return pasos
    
    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        return math.sqrt(dx**2 + dy**2)

if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)
    
    camino_p1_p2 = p1.camino(p2)
    print(camino_p1_p2)  # Imprime la lista de pasos entre p1 y p2
    
    distancia_p1_p2 = p1.distancia(p2)
    print(distancia_p1_p2)  # Imprime la distancia entre p1 y p2

         