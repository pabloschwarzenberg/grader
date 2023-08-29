class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        dif_x = self.x - otra_ciudad.x
        dif_y = self.y - otra_ciudad.y
        if dif_x > dif_y:
            maximo = dif_x
        else:
            maximo = dif_y

        pasos = []
        paso_x = dif_x / maximo
        paso_y = dif_y / maximo
        for i in range(abs(maximo)+1):
            pasos.append([self.x + paso_x*i, self.y + paso_y*i])

        return pasos

    def distancia(self, otra_ciudad):
        return ((self.x - otra_ciudad.x) ** 2 + (self.y - otra_ciudad.y) ** 2) ** (1/2)

if __name__ == "__main__":
    # Ejemplo de uso
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)
    print(p1.camino(p2))
    print(p1.distancia(p2))