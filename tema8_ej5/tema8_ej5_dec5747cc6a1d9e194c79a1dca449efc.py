import math

class Ciudad:
    def init(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

    def camino(self, otra_ciudad):
        ruta = []
        dx = otra_ciudad.coord_x - self.coord_x
        dy = otra_ciudad.coord_y - self.coord_y
        steps = max(abs(dx), abs(dy))
        if steps > 0:
            step_x = dx / steps
            step_y = dy / steps
            for i in range(steps + 1):
                x = self.coord_x + step_x * i
                y = self.coord_y + step_y * i
                ruta.append([x, y])
        return ruta

    def distancia(self, otra_ciudad):
        dx = otra_ciudad.coord_x - self.coord_x
        dy = otra_ciudad.coord_y - self.coord_y
        distancia = math.sqrt(dx2 + dy2)
        return distancia
