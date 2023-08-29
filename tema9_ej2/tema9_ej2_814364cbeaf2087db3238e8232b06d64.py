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
        if len(self.celdas[0]) != len(other.celdas):
            raise ValueError('Las matrices no tienen dimensiones compatibles para multiplicar')
        result = [[0 for j in range(len(other.celdas[0]))] for i in range(len(self.celdas))]
        for i in range(len(self.celdas)):
            for j in range(len(other.celdas[0])):
                for k in range(len(other.celdas)):
                    result[i][j] += self.celdas[i][k] * other.celdas[k][j]
        return Matriz(result)


if __name__ == "__main__":
    A = Matriz([[1, 2], [3, 4]])
    B = Matriz([[5, 6], [7, 8]])
    print(A * B)
