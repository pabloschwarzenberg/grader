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
            raise ValueError("Las matrices no se pueden multiplicar")

        filas_A = len(self.celdas)
        columnas_A = len(self.celdas[0])
        columnas_B = len(other.celdas[0])

        matriz_resultado = [[0] * columnas_B for _ in range(filas_A)]

        for i in range(filas_A):
            for j in range(columnas_B):
                for k in range(columnas_A):
                    matriz_resultado[i][j] += self.celdas[i][k] * other.celdas[k][j]

        return Matriz(matriz_resultado)


if __name__ == "__main__":
    a = Matriz([[1, 2], [3, 4]])
    b = Matriz([[5, 6], [7, 8]])
    r = a * b
    print(r)
