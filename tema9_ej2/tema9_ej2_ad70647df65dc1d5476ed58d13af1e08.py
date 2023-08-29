class Matriz:
    def __init__(self, celdas=[]):
        self.celdas = celdas

    def __repr__(self):
        s = ""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas[i])):
                s += "{0: >5} ".format(self.celdas[i][j])
            s += "\n"
        return s

    def __mul__(self, other):
        if len(self.celdas[0]) != len(other.celdas):
            raise ValueError("No se puede multiplicar las matrices. Las dimensiones no son válidas.")

        rows_self = len(self.celdas)
        cols_self = len(self.celdas[0])
        rows_other = len(other.celdas)
        cols_other = len(other.celdas[0])

        result = [[0 for _ in range(cols_other)] for _ in range(rows_self)]

        for i in range(rows_self):
            for j in range(cols_other):
                for k in range(cols_self):
                    result[i][j] += self.celdas[i][k] * other.celdas[k][j]

        return Matriz(result)

m1 = Matriz([[1, 2, 3], [4, 5, 6]])
m2 = Matriz([[7, 8], [9, 10], [11, 12]])

resultado = m1 * m2
print(resultado)
