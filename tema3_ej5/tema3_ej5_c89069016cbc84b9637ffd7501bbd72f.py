import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def camino(self, otra_ciudad):
        pasos = []
        current_x = self.x
        current_y = self.y

        while current_x != otra_ciudad.x or current_y != otra_ciudad.y:
            pasos.append([current_x, current_y])
            
            if current_x < otra_ciudad.x:
                current_x += 1
            elif current_x > otra_ciudad.x:
                current_x -= 1
            
            if current_y < otra_ciudad.y:
                current_y += 1
            elif current_y > otra_ciudad.y:
                current_y -= 1
        
        pasos.append([otra_ciudad.x, otra_ciudad.y])
        return pasos
    
    def distancia(self, otra_ciudad):
        distancia = math.sqrt((otra_ciudad.x - self.x)**2 + (otra_ciudad.y - self.y)**2)
        return round(distancia, 2)


# Ejemplo de uso
p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)

# Generar todos los pasos para llegar de p1 a p2
camino = p1.camino(p2)
print("Camino:", camino)

# Calcular la distancia recorrida
distancia = p1.distancia(p2)
print("Distancia:", distancia)
