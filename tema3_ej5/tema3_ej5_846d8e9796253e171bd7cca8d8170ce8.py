import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def camino(self, otra_ciudad):
        distancia_x = otra_ciudad.x - self.x
        distancia_y = otra_ciudad.y - self.y
        
        # Calcula la cantidad de pasos necesarios para llegar a la otra ciudad
        pasos = max(abs(distancia_x), abs(distancia_y))
        
        # Calcula el tamaño de cada paso en x e y
        paso_x = distancia_x / pasos
        paso_y = distancia_y / pasos
        
        # Genera la lista de puntos en el camino
        camino = []
        for i in range(pasos):
            x = round(self.x + i * paso_x)
            y = round(self.y + i * paso_y)
            camino.append([x, y])
        
        return camino
    
    def distancia(self, otra_ciudad):
        distancia_x = otra_ciudad.x - self.x
        distancia_y = otra_ciudad.y - self.y
        distancia = math.sqrt(distancia_x**2 + distancia_y**2)
        return round(distancia, 2)

# Ejemplo de uso
p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)

camino_p1_p2 = p1.camino(p2)
print(camino_p1_p2)  # [[1, 1], [2, 2], [3, 3]]

distancia_p1_p2 = p1.distancia(p2)
print(distancia_p1_p2)  # 2.83
