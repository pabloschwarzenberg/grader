import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def camino(self, destino):
        pasos = []
        diferencia_x = destino.x - self.x
        diferencia_y = destino.y - self.y
        pasos_totales = max(abs(diferencia_x), abs(diferencia_y))
        
        if diferencia_x != 0 and diferencia_y != 0:
            paso_x = diferencia_x / pasos_totales
            paso_y = diferencia_y / pasos_totales
            
            for i in range(pasos_totales):
                x = self.x + paso_x * (i+1)
                y = self.y + paso_y * (i+1)
                pasos.append([round(x, 2), round(y, 2)])
        elif diferencia_x != 0:
            paso_x = diferencia_x / pasos_totales
            
            for i in range(pasos_totales):
                x = self.x + paso_x * (i+1)
                pasos.append([round(x, 2), self.y])
        elif diferencia_y != 0:
            paso_y = diferencia_y / pasos_totales
            
            for i in range(pasos_totales):
                y = self.y + paso_y * (i+1)
                pasos.append([self.x, round(y, 2)])
        
        return pasos
    
    def distancia(self, destino):
        diferencia_x = destino.x - self.x
        diferencia_y = destino.y - self.y
        distancia = math.sqrt(diferencia_x**2 + diferencia_y**2)
        return round(distancia, 2)


p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)

camino_p1_p2 = p1.camino(p2)
print(camino_p1_p2)

distancia_p1_p2 = p1.distancia(p2)
print(distancia_p1_p2) 