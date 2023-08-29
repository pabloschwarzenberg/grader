class Ciudad:
  pass

if __name__ == "__main__":
  pass
import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        x_actual = self.x
        y_actual = self.y
        camino = [[x_actual, y_actual]]

        while x_actual != otra_ciudad.x or y_actual != otra_ciudad.y:
            if x_actual < otra_ciudad.x:
                x_actual += 1
            elif x_actual > otra_ciudad.x:
                x_actual -= 1

            if y_actual < otra_ciudad.y:
                y_actual += 1
            elif y_actual > otra_ciudad.y:
                y_actual -= 1

            camino.append([x_actual, y_actual])

        return camino

    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        distancia = math.sqrt(dx ** 2 + dy ** 2)
        return round(distancia, 2)

if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)

    recorrido = p1.camino(p2)
    print(recorrido)

    distancia_recorrida = p1.distancia(p2)
    print(distancia_recorrida)

         