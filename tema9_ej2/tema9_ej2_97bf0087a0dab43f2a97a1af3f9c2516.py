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
        if len(self.celdas[0]) != len(other.celdas):
            raise ValueError("No se pueden multiplicar las matrices. Las dimensiones no son válidas.")

        filas_a = len(self.celdas)
        columnas_a = len(self.celdas[0])
        columnas_b = len(other.celdas[0])

        resultado = [[0] * columnas_b for _ in range(filas_a)]

        for i in range(filas_a):
            for j in range(columnas_b):
                for k in range(columnas_a):
                    resultado[i][j] += self.celdas[i][k] * other.celdas[k][j]

        return Matriz(resultado)


if __name__ == "__main__":
    a = Matriz([[1, 2], [3, 4]])
    b = Matriz([[5, 6], [7, 8]])
    r = a * b
    print(r)