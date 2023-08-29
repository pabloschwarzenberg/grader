import math


class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def camino(self, o):
        posx = self.x
        posy = self.y
        lsta = []
        for i in range(max(abs(self.x-o.x), abs(self.y-o.y))):
            lsta.append([posx, posy])
            if posx < o.x:
                posx += 1
            elif posx > o.x:
                posx -= 1
            if posy < o.y:
                posy += 1
            elif posy > o.y:
                posy -= 1
        lsta.append([o.x, o.y])
        return lsta


if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)
    print(p1.camino(p2))
