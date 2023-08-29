import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, destino):
        camino = [[self.x, self.y]]
        current_x = self.x
        current_y = self.y

        while current_x != destino.x or current_y != destino.y:
            if current_x < destino.x:
                current_x += 1
            elif current_x > destino.x:
                current_x -= 1

            if current_y < destino.y:
                current_y += 1
            elif current_y > destino.y:
                current_y -= 1

            camino.append([current_x, current_y])

        return camino

    def distancia(self, destino):
        dx = abs(destino.x - self.x)
        dy = abs(destino.y - self.y)
        return math.sqrt(dx**2 + dy**2)

if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)

    ruta = p1.camino(p2)
    print(ruta)

    distancia = p1.distancia(p2)
    print(distancia)
         