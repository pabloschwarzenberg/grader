class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, other):
        d = ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** (1 / 2)
        return d

    def camino(self, other):
        camino = []
        x=self.x
        y=self.y
        while x != other.x or y != other.y:
            camino.append([x, y])
            if x != other.x:
                if x < other.x:
                    x += 1
                else:
                    x -= 1
            if y != other.y:
                if y < other.y:
                    y += 1
                else:
                    y -= 1
        camino.append([x, y])
        return camino
