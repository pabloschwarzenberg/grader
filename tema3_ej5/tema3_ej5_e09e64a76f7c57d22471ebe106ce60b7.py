import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def camino(self, otra_ciudad):
        distancia_x = abs(otra_ciudad.x - self.x)
        distancia_y = abs(otra_ciudad.y - self.y)
        distancia_total = max(distancia_x, distancia_y)
        pasos = []
        
        for i in range(distancia_total + 1):
            paso_x = self.x + int(round((distancia_x * i) / distancia_total))
            paso_y = self.y + int(round((distancia_y * i) / distancia_total))
            pasos.append([paso_x, paso_y])
        
        return pasos
    
    def distancia(self, otra_ciudad):
        distancia_x = abs(otra_ciudad.x - self.x)
        distancia_y = abs(otra_ciudad.y - self.y)
        distancia = math.sqrt(distancia_x**2 + distancia_y**2)
        return round(distancia, 2)

# Ejemplo de uso
p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)
pasos = p1.camino(p2)
distancia = p1.distancia(p2)

print("Pasos:")
for paso in pasos:
    print(paso)

print("Distancia recorrida:", distancia)
