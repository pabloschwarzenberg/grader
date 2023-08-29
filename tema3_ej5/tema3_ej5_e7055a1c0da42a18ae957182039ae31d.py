import math

class Ciudad:
    def _init_(self, x, y):
        self.x = x
        self.y = y
    
    def camino(self, otra_ciudad):
        x_diff = otra_ciudad.x - self.x
        y_diff = otra_ciudad.y - self.y
        steps = max(abs(x_diff), abs(y_diff))
        path = []
        for step in range(steps + 1):
            x = self.x + int(x_diff / steps * step)
            y = self.y + int(y_diff / steps * step)
            path.append([x, y])
        return path
    
    def distancia(self, otra_ciudad):
        x_diff = otra_ciudad.x - self.x
        y_diff = otra_ciudad.y - self.y
        return math.sqrt(x_diff * 2 + y_diff * 2)

# Ejemplo de uso
p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)

# Generar lista de pasos en el camino
camino_p1_p2 = p1.camino(p2)
print(camino_p1_p2)

# Calcular distancia recorrida
distancia_p1_p2 = p1.distancia(p2)
print(distancia_p1_p2)