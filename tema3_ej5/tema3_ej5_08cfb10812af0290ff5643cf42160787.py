class Ciudad:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def distancia(self, p2):
        distancia = ((self.x-p2.x)**2+(self.y-p2.y)**2)**(1/2)
        return distancia
         