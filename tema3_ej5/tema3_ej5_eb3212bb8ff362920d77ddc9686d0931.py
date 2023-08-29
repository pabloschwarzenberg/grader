import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        pasos = [[self.x, self.y]]
        curr_x = self.x
        curr_y = self.y

        while curr_x != otra_ciudad.x or curr_y != otra_ciudad.y:
            if curr_x < otra_ciudad.x:
                curr_x += 1
            elif curr_x > otra_ciudad.x:
                curr_x -= 1
            
            if curr_y < otra_ciudad.y:
                curr_y += 1
            elif curr_y > otra_ciudad.y:
                curr_y -= 1
            
            pasos.append([curr_x, curr_y])

        return pasos

    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        distancia = math.sqrt(dx**2 + dy**2)
        return round(distancia, 15)


if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)
    camino = p1.camino(p2)
    print("Camino:", camino)
    distancia = p1.distancia(p2)
    print("Distancia:", distancia)
