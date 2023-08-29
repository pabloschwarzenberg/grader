import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, destino):
        path = []
        current_x, current_y = self.x, self.y
        dest_x, dest_y = destino.x, destino.y

        while current_x != dest_x or current_y != dest_y:
            path.append([current_x, current_y])

            if current_x < dest_x:
                current_x += 1
            elif current_x > dest_x:
                current_x -= 1

            if current_y < dest_y:
                current_y += 1
            elif current_y > dest_y:
                current_y -= 1

        path.append([dest_x, dest_y])
        return path

    def distancia(self, destino):
        dx = abs(self.x - destino.x)
        dy = abs(self.y - destino.y)
        distance = math.sqrt(dx ** 2 + dy ** 2)
        return round(distance, 2)

p1 = Ciudad(1, 1)
p2 = Ciudad(3, 3)

camino_p1_p2 = p1.camino(p2)
distancia_p1_p2 = p1.distancia(p2)

print(camino_p1_p2)
print(distancia_p1_p2)
