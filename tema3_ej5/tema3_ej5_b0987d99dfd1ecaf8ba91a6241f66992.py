import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, ciudad_destino):
        camino = [[self.x, self.y]]
        x_actual = self.x
        y_actual = self.y

        while x_actual != ciudad_destino.x or y_actual != ciudad_destino.y:
            if x_actual < ciudad_destino.x:
                x_actual += 1
            elif x_actual > ciudad_destino.x:
                x_actual -= 1

            if y_actual < ciudad_destino.y:
                y_actual += 1
            elif y_actual > ciudad_destino.y:
                y_actual -= 1

            camino.append([x_actual, y_actual])

        return camino

    def distancia(self, ciudad_destino):
        dx = ciudad_destino.x - self.x
        dy = ciudad_destino.y - self.y
        distancia = math.sqrt(dx**2 + dy**2)
        return distancia

if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)

    funcion_camino = p1.camino
    camino = funcion_camino(p2)
    print(camino)

    funcion_distancia = p1.distancia
    distancia = funcion_distancia(p2)
    print(distancia)
         