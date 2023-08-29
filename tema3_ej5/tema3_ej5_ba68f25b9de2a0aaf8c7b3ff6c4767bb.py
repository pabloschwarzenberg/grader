import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, ciudad):
        pasos = []
        dx = ciudad.x - self.x
        dy = ciudad.y - self.y
        x = self.x
        y = self.y
        while x != ciudad.x or y != ciudad.y:
            if dx > 0:
                x += 1
                dx -= 1
            elif dx < 0:
                x -= 1
                dx += 1
            if dy > 0:
                y += 1
                dy -= 1
            elif dy < 0:
                y -= 1
                dy += 1
            pasos.append([x,y])
        return pasos

    def distancia(self, ciudad):
        dx = ciudad.x - self.x
        dy = ciudad.y - self.y
        return round(math.sqrt(dx*dx + dy*dy),2)

p1=Ciudad(1,1)
p2=Ciudad(3,3)
print(p1.camino(p2))
print(p1.distancia(p2))
