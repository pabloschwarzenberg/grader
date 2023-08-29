class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        print(self.distancia(otra_ciudad))
        lista = []
        for i in range(self.x, otra_ciudad.x + 1):
            for j in range(self.y, otra_ciudad.y + 1):
                lista.append([i, j])
        return lista

    def distancia(self, otra_ciudad):
        return (((otra_ciudad.x - self.x) * 2) + ((otra_ciudad.y - self.y) * 2)) ** (1 / 2)


p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)
print(p1.camino(p2))
print(p1.distancia(p2))
