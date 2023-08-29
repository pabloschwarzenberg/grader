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
        camino = []
        x1, y1 = self.x, self.y
        x2, y2 = otra_ciudad.x, otra_ciudad.y
        
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        step_x = -1 if x1 > x2 else 1
        step_y = -1 if y1 > y2 else 1
        error = dx - dy

        while x1 != x2 or y1 != y2:
            camino.append([x1, y1])
            error2 = 2 * error

            if error2 > -dy:
                error -= dy
                x1 += step_x

            if error2 < dx:
                error += dx
                y1 += step_y

        camino.append([x1, y1])
        return camino

    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        distancia = math.sqrt(dx ** 2 + dy ** 2)
        return (distancia)

p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)
camino_p1_p2 = p1.camino(p2)
distancia_p1_p2 = p1.distancia(p2)

print("Camino:", camino_p1_p2)
print("Distancia:", distancia_p1_p2)         