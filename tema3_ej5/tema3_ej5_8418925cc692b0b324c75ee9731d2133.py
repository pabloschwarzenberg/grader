from math import sqrt
class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pasos = [[x, y]]
        self.dc = 0
        self.n = 0

    def camino(self, otro):
        if (otro.x == self.x and otro.y != self.y):
            while otro.y != self.y:
                if otro.y > self.y:
                    self.y += 1
                    self.n += 1
                    self.pasos.append([self.x, self.y])
                else:
                    self.y -= 1
                    self.n += 1
                    self.pasos.append([self.x, self.y])
        elif otro.y == self.y and otro.x != self.x:
            while otro.x != self.x:
                if (otro.x > self.x):
                    self.x += 1
                    self.n += 1
                    self.pasos.append([self.x, self.y])
                else:
                    self.x -= 1
                    self.n += 1
                    self.pasos.append([self.x, self.y])
        elif otro.x != self.x and otro.y != self.y:
            while otro.x != self.x and otro.y != self.y:
                if (otro.y > self.y or otro.x > self.x):
                    if (otro.x != self.x):
                        self.y += 1
                        self.x += 1
                        self.dc += 1
                        self.pasos.append([self.x, self.y])
                        continue
                    self.y += 1
                    self.n += 1
                    self.pasos.append([self.x, self.y])

        return self.pasos

    def distancia(self, otro):
        return self.n + self.dc * sqrt(2)


if __name__ == "__main__":
    x1 = input()
    y1 = input()
    x2 = input()
    y2 = input()
    p1 = Ciudad(x1, y2)
    p2 = Ciudad(x2, y2)
    p1.camino(p2)
    p1.distancia(p2)