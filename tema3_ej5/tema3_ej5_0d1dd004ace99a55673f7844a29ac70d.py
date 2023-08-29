import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        distancia_x = otra_ciudad.x - self.x
        distancia_y = otra_ciudad.y - self.y

        pasos = abs(distancia_x) + abs(distancia_y)

        dx = 1 if distancia_x > 0 else -1
        dy = 1 if distancia_y > 0 else -1

        camino = []
        for _ in range(pasos):
            if distancia_x != 0 and distancia_y != 0:
                camino.append([self.x + dx, self.y + dy])
                self.x += dx
                self.y += dy
                distancia_x -= dx
                distancia_y -= dy
            elif distancia_x != 0:
                camino.append([self.x + dx, self.y])
                self.x += dx
                distancia_x -= dx
            elif distancia_y != 0:
                camino.append([self.x, self.y + dy])
                self.y += dy
                distancia_y -= dy

        return camino

    def distancia(self, otra_ciudad):
        distancia_x = otra_ciudad.x - self.x
        distancia_y = otra_ciudad.y - self.y

        distancia = math.sqrt(distancia_x ** 2 + distancia_y ** 2)
        return distancia


# Crear las ciudades p1 y p2
p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)

# Obtener el camino de p1 a p2
camino_p1_p2 = p1.camino(p2)

# Imprimir los pasos
for paso in camino_p1_p2:
    print(f"Paso: {paso}")

# Calcular y mostrar la distancia recorrida
distancia_recorrida = p1.distancia(p2)
print("Distancia recorrida:", distancia_recorrida)
