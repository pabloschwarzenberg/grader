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
        pasos = []
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        max_delta = max(abs(dx), abs(dy))
        step_x = dx / max_delta
        step_y = dy / max_delta

        for i in range(max_delta + 1):
            x = self.x + round(step_x * i)
            y = self.y + round(step_y * i)
            pasos.append([x, y])

        return pasos

    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        distancia = math.sqrt(dx ** 2 + dy ** 2)
        return round(distancia, 2)
         