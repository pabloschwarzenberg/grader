class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        pasos = []
        x_actual = self.x
        y_actual = self.y
        while x_actual != otra_ciudad.x or y_actual != otra_ciudad.y:
            pasos.append([x_actual, y_actual])
            if x_actual < otra_ciudad.x:
                x_actual += 1
            elif x_actual > otra_ciudad.x:
                x_actual -= 1
            if y_actual < otra_ciudad.y:
                y_actual += 1
            elif y_actual > otra_ciudad.y:
                y_actual -= 1
        pasos.append([x_actual, y_actual])
        return pasos

    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        distancia = ((dx ** 2) + (dy ** 2)) ** 0.5
        return round(distancia, 16)


if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)    
    camino = p1.camino(p2)
    distancia = p1.distancia(p2)
    print(p1.distancia(p2))
