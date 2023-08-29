class Matriz:
    def __init__(self, celdas=[]):
        self.celdas = celdas

    def __repr__(self):
        s = ""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s += "{0: >5}".format(self.celdas[i][j])
            s += "\n"
        return s

    def __mult__(self, other):
        celdas = []
        for i in range(len(self.celdas)):
          subceldas = []
          for j in range(len(other.celdas)):
            suma = 0
            for k in range(len(self.celdas)):
              print(suma)
              suma += self.celdas[i][k]*other.celdas[k][j]
            print()
            subceldas += [suma]
          celdas = celdas + [subceldas]
        self.celdas = celdas
        return self