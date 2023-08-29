class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        pasos = []
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        distancia = max(abs(dx), abs(dy))

        for i in range(distancia + 1):
            paso_x = self.x + int(i * dx / distancia)
            paso_y = self.y + int(i * dy / distancia)
            pasos.append([paso_x, paso_y])

        return pasos

    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        distancia = (dx ** 2 + dy ** 2) ** 0.5
        return distancia


# Ejemplo de uso
p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)

lista_pasos = p1.camino(p2)
print(lista_pasos)

distancia_recorrida = p1.distancia(p2)
print(distancia_recorrida)
