class Matriz:
    def __init__(self, celdas):
        self.celdas = celdas

    def __repr__(self):
        s = ""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s += "{0: >5} ".format(self.celdas[i][j])
            s += "\n"
        return s

    def __mul__(self, other):
        resultante = []
        i = 0
        j = 0
        dim1 = len(self.celdas)
        while i < dim1:
            fila = []
            while j < dim1:
                fila.append(self.celdas[i][j] * other.celdas[i][j])
                j += 1
            resultante.append(fila)
            i += 1
        return Matriz(resultante)


if __name__ == "__main__":
    a = Matriz([[1, 2], [3, 4]])
    b = Matriz([[5, 6], [7, 8]])
    r = a * b
    print(r)
