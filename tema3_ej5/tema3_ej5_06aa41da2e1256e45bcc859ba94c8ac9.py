import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        pasos = []
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        steps = max(abs(dx), abs(dy))
        if steps > 0:
            x_step = dx / steps
            y_step = dy / steps
            for i in range(steps):
                x = self.x + x_step * i
                y = self.y + y_step * i
                pasos.append([round(x), round(y)])
        pasos.append([otra_ciudad.x, otra_ciudad.y])
        return pasos

    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        distancia = math.sqrt(dx**2 + dy**2)
        return round(distancia, 8)  # Redondear a 8 decimales

if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)

    pasos = p1.camino(p2)
    print("Pasos:", pasos)

    distancia = p1.distancia(p2)
    print("Distancia:", distancia)
