import math


class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        pasos = []
        current_x, current_y = self.x, self.y
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
        dx = abs(self.x - otra_ciudad.x)
        dy = abs(self.y - otra_ciudad.y)
        distancia = math.sqrt(dx ** 2 + dy ** 2)
        return (distancia, 2)

