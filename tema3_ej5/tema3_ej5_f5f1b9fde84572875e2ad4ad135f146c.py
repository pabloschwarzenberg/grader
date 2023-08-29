import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        # Generar todos los pasos necesarios para llegar de una ciudad a la otra
        # utilizando movimientos diagonales
        distancia_x = abs(otra_ciudad.x - self.x)
        distancia_y = abs(otra_ciudad.y - self.y)
        pasos = max(distancia_x, distancia_y)

        # Generar la lista de puntos
        camino = []
        for paso in range(pasos + 1):
            x = self.x + (distancia_x // pasos) * paso
            y = self.y + (distancia_y // pasos) * paso
            camino.append([x, y])

        # Verificar que el camino comienza y termina en las ciudades correctas
        if camino[0] != [self.x, self.y] or camino[-1] != [otra_ciudad.x, otra_ciudad.y]:
            raise ValueError("El camino generado no es válido")

        # Imprimir los pasos
        for punto in camino:
            print(punto)

    def distancia(self, otra_ciudad):
        # Calcular la distancia euclidiana entre dos ciudades
        distancia_x = abs(otra_ciudad.x - self.x)
        distancia_y = abs(otra_ciudad.y - self.y)
        distancia = math.sqrt(distancia_x ** 2 + distancia_y ** 2)
        return round(distancia, 2)


# Ejemplo de uso
p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)

print("Camino:")
p1.camino(p2)

print("\nDistancia:", p1.distancia(p2))

         