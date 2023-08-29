import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def camino(self, otra_ciudad):
        pasos = []
        diferencia_x = otra_ciudad.x - self.x
        diferencia_y = otra_ciudad.y - self.y
        pasos_totales = max(abs(diferencia_x), abs(diferencia_y))
        paso_x = diferencia_x / pasos_totales
        paso_y = diferencia_y / pasos_totales
        
        for i in range(pasos_totales):
            x = round(self.x + i * paso_x)
            y = round(self.y + i * paso_y)
            pasos.append([x, y])
        pasos.append([otra_ciudad.x, otra_ciudad.y])
        return pasos
    
    def distancia(self, otra_ciudad):
        diferencia_x = otra_ciudad.x - self.x
        diferencia_y = otra_ciudad.y - self.y
        distancia = math.sqrt(diferencia_x * 2 + diferencia_y * 2)
        return distancia

if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)
    camino_p1_p2 = p1.camino(p2)
    print(camino_p1_p2)
    distancia_p1_p2 = p1.distancia(p2)
    print(distancia_p1_p2)         