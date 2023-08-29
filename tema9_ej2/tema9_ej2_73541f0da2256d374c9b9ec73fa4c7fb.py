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
        if len(self.celdas) == 0 or len(other.celdas) == 0:
            return Matriz()  

        rows_a = len(self.celdas)
        cols_a = len(self.celdas[0])
        rows_b = len(other.celdas)
        cols_b = len(other.celdas[0])

        if cols_a != rows_b:
            raise ValueError("El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.")

        result = Matriz([[0] * cols_b for _ in range(rows_a)])

        for i in range(rows_a):
            for j in range(cols_b):
                for k in range(cols_a):
                    result.celdas[i][j] += self.celdas[i][k] * other.celdas[k][j]

        return result

if __name__ == "__main__":
    a = Matriz([[1, 2], [3, 4]])
    b = Matriz([[5, 6], [7, 8]])
    r = a * b
    print(r)
