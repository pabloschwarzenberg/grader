import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def camino(self, otra_ciudad):
        # Calcular la diferencia en coordenadas
        diff_x = otra_ciudad.x - self.x
        diff_y = otra_ciudad.y - self.y
        
        # Calcular la distancia total
        distancia_total = max(abs(diff_x), abs(diff_y))
        
        # Calcular los pasos necesarios para llegar de una ciudad a la otra
        pasos = []
        x = self.x
        y = self.y
        
        for _ in range(distancia_total):
            if diff_x > 0:
                x += 1
                diff_x -= 1
            elif diff_x < 0:
                x -= 1
                diff_x += 1
            
            if diff_y > 0:
                y += 1
                diff_y -= 1
            elif diff_y < 0:
                y -= 1
                diff_y += 1
            
            pasos.append([x, y])
        
        # Imprimir los pasos necesarios
        for paso in pasos:
            print(paso)
        
        return pasos
    
    def distancia(self, otra_ciudad):
        diff_x = otra_ciudad.x - self.x
        diff_y = otra_ciudad.y - self.y
        distancia = math.sqrt(diff_x**2 + diff_y**2)
        return round(distancia, 2)
