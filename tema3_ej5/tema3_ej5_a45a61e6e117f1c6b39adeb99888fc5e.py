import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, destino):
        camino_puntos = []
        x_actual = self.x
        y_actual = self.y

        while x_actual != destino.x or y_actual != destino.y:
            camino_puntos.append([x_actual, y_actual])
            if x_actual < destino.x:
                x_actual += 1
            elif x_actual > destino.x:
                x_actual -= 1

            if y_actual < destino.y:
                y_actual += 1
            elif y_actual > destino.y:
                y_actual -= 1

        camino_puntos.append([destino.x, destino.y])

        print(camino_puntos)

    def distancia(self, destino):
        distancia = math.sqrt((self.x - destino.x) ** 2 + (self.y - destino.y) ** 2)
        return round(distancia, 2)

# Ejemplo de uso
p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)

p1.camino(p2)
distancia = p1.distancia(p2)
print(distancia)
