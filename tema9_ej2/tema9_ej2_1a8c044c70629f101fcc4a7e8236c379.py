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
            raise ValueError("Las dimensiones de las matrices no son compatibles para la multiplicación.")

        filas_a = len(self.celdas)
        columnas_a = len(self.celdas[0])
        filas_b = len(other.celdas)
        columnas_b = len(other.celdas[0])

        resultado = [[0] * columnas_b for _ in range(filas_a)]

        for i in range(filas_a):
            for j in range(columnas_b):
                for k in range(columnas_a):
                    resultado[i][j] += self.celdas[i][k] * other.celdas[k][j]

        return Matriz(resultado)


if __name__ == "__main__":
    matriz_a = Matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matriz_b = Matriz([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
    resultado = matriz_a * matriz_b
    print(resultado)

