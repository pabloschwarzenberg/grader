import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        x_actual = self.x
        y_actual = self.y
        x_destino = otra_ciudad.x
        y_destino = otra_ciudad.y

        pasos = [[x_actual, y_actual]]

        while x_actual != x_destino or y_actual != y_destino:
            if x_actual < x_destino:
                x_actual += 1
            elif x_actual > x_destino:
                x_actual -= 1

            if y_actual < y_destino:
                y_actual += 1
            elif y_actual > y_destino:
                y_actual -= 1

            pasos.append([x_actual, y_actual])

        return pasos

    def distancia(self, otra_ciudad):
        distancia_x = abs(self.x - otra_ciudad.x)
        distancia_y = abs(self.y - otra_ciudad.y)
        distancia = math.sqrt(distancia_x**2 + distancia_y**2)
        return round(distancia, 16)


# Ejemplo de uso
p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)

# Generar los pasos para llegar de p1 a p2
pasos = p1.camino(p2)
print(pasos)

# Calcular la distancia recorrida de p1 a p2
distancia = p1.distancia(p2)
print(distancia)


