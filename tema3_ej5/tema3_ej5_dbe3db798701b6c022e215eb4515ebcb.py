import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, other):
        camino = []
        current_x = self.x
        current_y = self.y

        while current_x != other.x or current_y != other.y:
            camino.append([current_x, current_y])

            if current_x < other.x:
                current_x += 1
            elif current_x > other.x:
                current_x -= 1

            if current_y < other.y:
                current_y += 1
            elif current_y > other.y:
                current_y -= 1

        camino.append([current_x, current_y])
        return camino

    def distancia(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        distancia = math.sqrt(dx**2 + dy**2)
        return distancia


if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)
    camino = p1.camino(p2)
    distancia = p1.distancia(p2)

    print("Camino:", camino)
    print("Distancia:", distancia)
         