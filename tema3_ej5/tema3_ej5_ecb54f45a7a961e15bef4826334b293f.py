class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.caminos = [["",""],["",""],["",""]]

    def distancia(self, other):
        magia = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        l = list(str(magia))
        resultados2 = []
        for i in range(0, 4):
            resultados2.append(l[i])
        resultados = "".join(resultados2)
        resultados = float(resultados)
        print(resultados)

    def camino(self,other):
        self.caminos[0][0] = self.x
        self.caminos[0][1] = self.y
        self.caminos[1][0] = int((other.x + self.x) / 2)
        self.caminos[1][1] = int((other.y + self.y) / 2)
        self.caminos[2][0] = other.x
        self.caminos[2][1] = other.y
        print(self.caminos)

if __name__ == "__main__":
  p1=Ciudad(1,1)
  p2=Ciudad(3,3)
  p1.camino(p2)
  p1.distancia(p2)
         