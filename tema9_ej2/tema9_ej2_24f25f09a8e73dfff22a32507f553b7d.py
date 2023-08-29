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
            raise ValueError("The number of columns in the first matrix must be equal to the number of rows in the second matrix.")

        result = []
        for i in range(len(self.celdas)):
            row = []
            for j in range(len(other.celdas[0])):
                element = 0
                for k in range(len(other.celdas)):
                    element += self.celdas[i][k] * other.celdas[k][j]
                row.append(element)
            result.append(row)

        return Matriz(result)