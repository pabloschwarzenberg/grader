class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        pasos = []
        x_actual = self.x
        y_actual = self.y
        x_destino = otra_ciudad.x
        y_destino = otra_ciudad.y

        while x_actual != x_destino or y_actual != y_destino:
            pasos.append([x_actual, y_actual])
            
            if x_actual < x_destino:
                x_actual += 1
            elif x_actual > x_destino:
                x_actual -= 1
            
            if y_actual < y_destino:
                y_actual += 1
            elif y_actual > y_destino:
                y_actual -= 1

        pasos.append([x_actual, y_actual])  # Agregar la ciudad destino a los pasos
        return pasos

    def distancia(self, otra_ciudad):
        distancia_x = otra_ciudad.x - self.x
        distancia_y = otra_ciudad.y - self.y
        distancia = ((distancia_x ** 2) + (distancia_y ** 2)) ** 0.5
        return round(distancia, 16)