from math import sqrt


class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, other):
        delta_y = other.y - self.y
        delta_x = other.x - self.x
        x = self.x
        y = self.y
        trayectoria = [[x, y]]
        if delta_x != 0:
            pendiente = delta_y / delta_x
            while x != other.x:
                x += 1
                y += int(pendiente)
                trayectoria.append([x, y])
        else:
            while y != other.y:
                y += 1
                trayectoria.append([x, y])
        return trayectoria

    def distancia(self, other):
        delta_y = other.y - self.y
        delta_x = other.x - self.x
        # Distancia punto-punto.
        distancia = float(sqrt(delta_x ** 2 + delta_y ** 2))
        return distancia

if __name__ == '__main__':
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)
    trayecto = p1.camino(p2)
    recorrido = p1.distancia(p2)
    print('Hay que pasar por los puntos', trayecto, 'recorriendo una distancia', recorrido)
