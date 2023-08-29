class Ciudad:
    def __init__(self, xx, yy):
        self.x = xx
        self.y = yy

    def camino(self, other):
        A = [self.x, self.y]
        B = [other.x, other.y]
        camino = [abs(int(self.x - other.x)), abs(int(other.y - self.y))]
        return [A,camino,B]

    def distancia(self,other):
        ejex = (self.x - other.x)**2
        ejey = (self.y - other.y)**2
        distancia = (ejex + ejey)**(1/2)
        return distancia
         