import math
class Ciudad:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.recorrido=[[x, y]]
        self.D=0
        self.M = 0

    def camino(self, other):
        if other.x==self.x and other.y != self.y:
            while other.y != self.y:
                if other.y > self.y:
                    self.y += 1
                    self.M += 1
                    self.recorrido.append([self.x, self.y])
                else:
                    self.y -= 1
                    self.M += 1
                    self.recorrido.append([self.x, self.y])
        elif other.y == self.y and other.x != self.x:
            while other.x != self.x:
                if other.x > self.x:
                    self.x += 1
                    self.M += 1
                    self.recorrido.append([self.x, self.y])
                else:
                    self.x -= 1
                    self.M += 1
                    self.recorrido.append([self.x, self.y])
        elif other.x != self.x and other.y != self.y:
            while other.x != self.x and other.y != self.y:
                if other.y > self.y or other.x > self.x:
                    if other.x != self.x:
                        self.y += 1
                        self.x += 1
                        self.D += 1
                        self.recorrido.append([self.x, self.y])
                        continue
                    self.y += 1
                    self.M += 1
                    self.recorrido.append([self.x, self.y])

        return self.recorrido

    def distancia(self, other):
        return self.M + self.D * math.sqrt(2)


if __name__ == "__main__":
    x1 = input()
    y1 = input()
    x2 = input()
    y2 = input()
    p1 = Ciudad(x1, y2)
    p2 = Ciudad(x2, y2)
    p1.camino(p2)
    p1.distancia(p2)