import math
class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def camino(self, p2):
        l = [[self.x, self.y]]
        x = self.x
        y = self.y
        while p2.x != x and p2.y != y:
            if p2.x < x:
                x -= 1
            elif p2.x > x:
                x += 1

            if p2.y < y:
                y -= 1
            elif p2.y > y:
                y += 1

            l.append([x, y])
        return l
            
    
    def distancia(self, p2):
        return math.sqrt((self.x-p2.x)**2 + (self.y-p2.y)**2)
