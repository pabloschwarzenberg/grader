class Matriz:
    def __init__(self, celdas=[]):
        self.celdas = celdas

    def __repr__(self):
        s = ""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s += "{0: >5} ".format(self.celdas[i][j])
            s += "\n"
        return s

    def __mul__(self, other):
        celdas1 = []
        for celda in self.celdas:
            celda0 = []
            for j in range(len(other.celdas)):
                k = 0
                for i in range(len(self.celdas)):
                    k += celda[i] * other.celdas[i][j]
                celda0.append(k)
            celdas1.append(celda0)

        return Matriz(celdas1)


if __name__ == "__main__":
    a = Matriz([[1, 2],
                [3, 4]])

    b = Matriz([[5, 6],
                [7, 8]])
    r = a * b
    print(r)
