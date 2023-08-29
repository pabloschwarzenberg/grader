import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def camino(self, otra_ciudad):
        # Calcula los pasos necesarios para llegar de una ciudad a la otra
        pasos = []
        distancia_x = otra_ciudad.x - self.x
        distancia_y = otra_ciudad.y - self.y
        paso_x = 1 if distancia_x > 0 else -1
        paso_y = 1 if distancia_y > 0 else -1

        while self.x != otra_ciudad.x or self.y != otra_ciudad.y:
            self.x += paso_x
            self.y += paso_y
            pasos.append([self.x, self.y])
        
        return pasos
    
    def distancia(self, otra_ciudad):
        # Calcula la distancia entre dos ciudades utilizando el teorema de Pitágoras
        distancia_x = otra_ciudad.x - self.x
        distancia_y = otra_ciudad.y - self.y
        distancia = math.sqrt(distancia_x**2 + distancia_y**2)
        return round(distancia, 2)

# Ejemplo de uso
p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)

camino = p1.camino(p2)
distancia = p1.distancia(p2)

print(camino)  # [[1, 1], [2, 2], [3, 3]]
print(distancia)  # 2.82
