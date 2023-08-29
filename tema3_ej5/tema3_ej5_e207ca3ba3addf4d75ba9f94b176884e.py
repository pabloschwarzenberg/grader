import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y

        distancia = max(abs(dx), abs(dy))

        if dx > 0:
            dir_x = "derecha"
        else:
            dir_x = "izquierda"

        if dy > 0:
            dir_y = "arriba"
        else:
            dir_y = "abajo"

        pasos_x = [dir_x] * abs(dx)
        pasos_y = [dir_y] * abs(dy)

        pasos = pasos_x + pasos_y

        for paso in pasos:
            print("Ir", paso)

        return distancia

    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y

        distancia = math.sqrt(dx**2 + dy**2)
        return distancia


# Ejemplo de uso
p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)

print("Pasos para llegar de p1 a p2:")
distancia_recorrida = p1.camino(p2)
print("Distancia recorrida:", distancia_recorrida)
