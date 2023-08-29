import math

class Ciudad:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, other):
        puntos = []
        puntos.append([self.x, self.y])
        ## avance en x
        dx = other.x - self.x
        step_x = 0
        while abs(step_x) < abs(dx):
            step_x = step_x + dx/(abs(dx))
            puntos.append([self.x + int(step_x), self.y])
        ## avance en y
        dy = other.y - self.y
        last_step_x = puntos[-1][0]
        step_y = 0
        while abs(step_y) < abs(dy):
            step_y = step_y + dy/(abs(dy))
            puntos.append([last_step_x, self.y + int(step_y)])

        return puntos

    def distancia(self, other):
        distancia = ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
        return distancia

if __name__ == "__main__":
  pass         