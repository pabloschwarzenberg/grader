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

        rows_self = len(self.celdas)
        cols_self = len(self.celdas[0])
        rows_other = len(other.celdas)
        cols_other = len(other.celdas[0])

        if cols_self != rows_other:
            return Matriz()

        result = Matriz([[0] * cols_other for _ in range(rows_self)])

        for i in range(rows_self):
            for j in range(cols_other):
                for k in range(cols_self):
                    result.celdas[i][j] += self.celdas[i][k] * other.celdas[k][j]

        return result


if __name__ == "__main__":
    m1 = Matriz([[1, 2], [3, 4]])
    m2 = Matriz([[5, 6], [7, 8]])
    print("Matriz 1:")
    print(m1)
    print("Matriz 2:")
    print(m2)
    print("Multiplicación de matrices:")
    print(m1 * m2)

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           