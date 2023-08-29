class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, other):
        coordenadas = []
        if self.x > other.x:
            mayorx = self.x
            menorx = other.x
        else:
            mayorx = other.x
            menorx = self.x
        if self.y > other.y:
            mayory = self.y
            menory = other.y
        else:
            mayory = other.y
            menory = self.y
        if mayorx > mayory:
            mayor = mayorx
        else:
            mayor = mayory
        for i in range(mayor):
            coordenadas.append([])
            coordenadas[i].append(menorx)
            coordenadas[i].append(menory)
            if menorx != mayorx:
                menorx += 1
            if menory != mayory:
                menory += 1
            print(coordenadas)
        return coordenadas

    def distancia(self, p2):
        distancia_recorrida = self.camino(p2)
        distancia = 0
        for i in range(len(distancia_recorrida)-1):
            i += 1
            distancia_1 = 0
            for j in range(len(distancia_recorrida[i])):
                j = distancia_recorrida[i][j] - distancia_recorrida[i-1][j]
                distancia_1 += j ** 2
            distancia_1 = distancia_1 ** 0.5
            distancia += distancia_1
        return distancia


if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)
    p1.camino(p2)
    p1.distancia(p2)


         