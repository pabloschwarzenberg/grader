class Ciudad:
    def __init__(self, x, y):
        self.xo = x
        self.yo = y
        self.x = x
        self.y = y

    def camino(self, other):
        camino = []
        terminado = False
        while not terminado:
            if self.x == other.x and self.y == other.y:
                terminado = True

            paso = []
            if self.x < other.x:
                paso.append(self.x)
                self.x += 1

            elif other.x < self.x:
                paso.append(other.x)
                other.x += 1

            else:
                paso.append(self.x)

            if self.y < other.y:
                paso.append(self.y)
                self.y += 1

            elif other.y < self.y:
                paso.append(other.y)
                other.y += 1

            else:
                paso.append(self.y)

            camino.append(paso)

        return camino

    def distancia(self, other):
        distancia = ((self.xo-other.xo)**2 + (self.yo-other.yo)**2)**(1/2)
        return distancia
