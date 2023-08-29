import math
class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, p2):
        x1 = self.x
        y1 = self.y
        x2 = p2.x
        y2 = p2.y
        x3 = abs(x1-x2) + 1
        y3 = abs(y1-y2) + 1
        z = max(x3, y3)
        lista1 = []
        for i in range(z):
            lista1.append([])
        lista1[0].append(x1)
        lista1[0].append(y1)
        contador = 1
        for i in range(1,z):
            while x1 != x2:
                if x1 > x2:
                    x1 -= 1
                    lista1[contador].append(x1)
                if x1 < x2:
                    x1 += 1
                    lista1[contador].append(x1)
                contador +=1
            if x1 == x2:
                try:
                    lista1[contador].append(x1)
                except:
                    break
                contador += 1
        contador = 1
        for i in range(z):
            while y1 != y2:
                if y1 > y2:
                    y1 -= 1
                    lista1[contador].append(y1)
                if y1 < y2:
                    y1 += 1
                    lista1[contador].append(y1)
                contador += 1
            if y1 == y2:
                try:
                    lista1[contador].append(y1)
                except:
                    break
                contador += 1
        return lista1
    def distancia(self, p2):
        x1 = self.x
        y1 = self.y
        x2 = p2.x
        y2 = p2.y
        x3 = abs(x1 - x2) + 1
        y3 = abs(y1 - y2) + 1
        z = max(x3, y3)
        lista1 = []
        for i in range(z):
            lista1.append([])
        lista1[0].append(x1)
        lista1[0].append(y1)
        contador = 1
        for i in range(1, z):
            while x1 != x2:
                if x1 > x2:
                    x1 -= 1
                    lista1[contador].append(x1)
                if x1 < x2:
                    x1 += 1
                    lista1[contador].append(x1)
                contador += 1
            if x1 == x2:
                try:
                    lista1[contador].append(x1)
                except:
                    break
                contador += 1
        contador = 1
        for i in range(z):
            while y1 != y2:
                if y1 > y2:
                    y1 -= 1
                    lista1[contador].append(y1)
                if y1 < y2:
                    y1 += 1
                    lista1[contador].append(y1)
                contador += 1
            if y1 == y2:
                try:
                    lista1[contador].append(y1)
                except:
                    break
                contador += 1
        distancia = 0
        for i in range(0,z-1):
            p1 = lista1[i]
            p2 = lista1[i+1]
            if p1[0] == p2[0] and p1[1] != p2[1]:
                distancia += 1
            if p1[0] != p2[0] and p1[1] == p2[1]:
                distancia += 1
            if p1[0] != p2[0] and p1[1] != p2[1]:
                distancia += math.sqrt(2)
          
        return distancia
