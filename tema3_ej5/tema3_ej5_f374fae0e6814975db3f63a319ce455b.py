import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        camino = []
        current_x = self.x
        current_y = self.y

        while current_x != otra_ciudad.x or current_y != otra_ciudad.y:
            camino.append([current_x, current_y])

            if current_x < otra_ciudad.x:
                current_x += 1
            elif current_x > otra_ciudad.x:
                current_x -= 1

            if current_y < otra_ciudad.y:
                current_y += 1
            elif current_y > otra_ciudad.y:
                current_y -= 1

        camino.append([otra_ciudad.x, otra_ciudad.y])

        return camino

    def distancia(self, otra_ciudad):
        distancia = math.sqrt((otra_ciudad.x - self.x)**2 + (otra_ciudad.y - self.y)**2)
        return round(distancia, 2)

if __name__ == "__main__":
    x1 = int(input("Ingrese la coordenada x de la primera ciudad: "))
    y1 = int(input("Ingrese la coordenada y de la primera ciudad: "))
    x2 = int(input("Ingrese la coordenada x de la segunda ciudad: "))
    y2 = int(input("Ingrese la coordenada y de la segunda ciudad: "))

    ciudad1 = Ciudad(x1, y1)
    ciudad2 = Ciudad(x2, y2)

    camino = ciudad1.camino(ciudad2)
    print("Camino:", camino)

    distancia = ciudad1.distancia(ciudad2)
    print("Distancia:", distancia)