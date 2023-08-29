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
            raise ValueError("Las matrices no tienen dimensiones compatibles para la multiplicación")

        filas_a = len(self.celdas)
        columnas_b = len(other.celdas[0])
        resultado = Matriz([[0] * columnas_b for _ in range(filas_a)])

        for i in range(filas_a):
            for j in range(columnas_b):
                for k in range(len(other.celdas)):
                    resultado.celdas[i][j] += self.celdas[i][k] * other.celdas[k][j]

        return resultado


if __name__ == "__main__":
    a = Matriz([[1, 2], [3, 4]])
    b = Matriz([[5, 6], [7, 8]])
    r = a * b
    print(r)
