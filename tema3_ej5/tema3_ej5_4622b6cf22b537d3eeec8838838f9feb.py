import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, ciudad_destino):
        distancia_x = ciudad_destino.x - self.x
        distancia_y = ciudad_destino.y - self.y

        # Determinar la dirección de los pasos en x y y
        direccion_x = 1 if distancia_x > 0 else -1
        direccion_y = 1 if distancia_y > 0 else -1

        # Calcular la cantidad de pasos necesarios en x y y
        pasos_x = abs(distancia_x)
        pasos_y = abs(distancia_y)

        # Calcular la distancia diagonal
        distancia_diagonal = min(pasos_x, pasos_y)

        # Generar la lista de puntos del camino
        camino = [[self.x, self.y]]
        for i in range(distancia_diagonal):
            punto = [self.x + (i + 1) * direccion_x, self.y + (i + 1) * direccion_y]
            camino.append(punto)

        # Completar con los pasos restantes en x o y
        if pasos_x > pasos_y:
            for i in range(distancia_diagonal, pasos_x):
                punto = [self.x + (i + 1) * direccion_x, self.y]
                camino.append(punto)
        elif pasos_y > pasos_x:
            for i in range(distancia_diagonal, pasos_y):
                punto = [self.x, self.y + (i + 1) * direccion_y]
                camino.append(punto)

        camino.append([ciudad_destino.x, ciudad_destino.y])

        return camino

    def distancia(self, ciudad_destino):
        distancia_x = ciudad_destino.x - self.x
        distancia_y = ciudad_destino.y - self.y
        distancia = math.sqrt(distancia_x ** 2 + distancia_y ** 2)
        return round(distancia, 8)

if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)

    camino_p1_p2 = p1.camino(p2)
    print(camino_p1_p2)

    distancia_p1_p2 = p1.distancia(p2)
    print(distancia_p1_p2)

         