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
        if len(self.celdas) == 0 or len(other.celdas) == 0:
            return Matriz()

        m = len(self.celdas)
        n = len(other.celdas[0])
        p = len(other.celdas)

        if len(self.celdas[0]) != p:
            return Matriz()

        result = []
        for i in range(m):
            row = []
            for j in range(n):
                value = 0
                for k in range(p):
                    value += self.celdas[i][k] * other.celdas[k][j]
                row.append(value)
            result.append(row)

        return Matriz(result)


if __name__ == "__main__":
    a = Matriz([[1, 2], [3, 4]])
    b = Matriz([[5, 6], [7, 8]])
    r = a * b
    print(r)

           