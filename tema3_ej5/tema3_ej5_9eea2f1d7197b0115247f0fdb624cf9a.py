class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, other):
        coordenadas = []
        coordenadas.append([self.x, self.y])
        x = other.x-self.x
        y = other.y-self.y
        coordenadas.append([x, y])
        coordenadas.append([other.x, other.y])

        return coordenadas

    def distancia(self, other):
        d = ((self.y-other.y)**2+(self.x-other.x)**2)**(1/2)

        return d

if __name__ == "__main__":
  a = input()
  b = input()
  p1 = Ciudad(a)
  p2 = Ciudad(b)
  print(p1.camino(p2))
  print(p1.distancia(p2))
