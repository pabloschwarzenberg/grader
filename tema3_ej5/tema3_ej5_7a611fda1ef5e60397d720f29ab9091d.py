import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        distancia_x = otra_ciudad.x - self.x
        distancia_y = otra_ciudad.y - self.y

        direccion_x = "derecha" if distancia_x > 0 else "izquierda"
        direccion_y = "arriba" if distancia_y > 0 else "abajo"

        pasos_x = abs(distancia_x)
        pasos_y = abs(distancia_y)

        pasos_diagonal = min(pasos_x, pasos_y)
        pasos_rectos = abs(pasos_x - pasos_y)

        for i in range(pasos_diagonal):
            print(f"Ir {direccion_x}-{direccion_y} (diagonal)")
        for i in range(pasos_rectos):
            if pasos_x > pasos_y:
                print(f"Ir {direccion_x} (recto)")
            else:
                print(f"Ir {direccion_y} (recto)")

    def distancia(self, otra_ciudad):
        distancia_x = otra_ciudad.x - self.x
        distancia_y = otra_ciudad.y - self.y
        distancia = math.sqrt(distancia_x ** 2 + distancia_y ** 2)
        return distancia

# Ejemplo de uso
p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)
p1.camino(p2)

distancia_recorrida = p1.distancia(p2)
print(f"Distancia recorrida: {distancia_recorrida}")
