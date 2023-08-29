class Matriz:
    def __init__(self, celdas=[]):
        self.celdas = celdas

    def __repr__(self):
        s = ""
        for fila in self.celdas:
            for celda in fila:
                s += "{0: >5} ".format(celda)
            s += "\n"
        return s

    def __mul__(self, other):
        if len(self.celdas[0]) != len(other.celdas):
            raise ValueError("El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.")

        filas_A = len(self.celdas)
        columnas_A = len(self.celdas[0])
        filas_B = len(other.celdas)
        columnas_B = len(other.celdas[0])

        # Crear una matriz de ceros para almacenar el resultado
        resultado = [[0 for _ in range(columnas_B)] for _ in range(filas_A)]

        # Realizar la multiplicación de matrices
        for i in range(filas_A):
            for j in range(columnas_B):
                for k in range(columnas_A):
                    resultado[i][j] += self.celdas[i][k] * other.celdas[k][j]

        return Matriz(resultado)


if __name__ == "__main__":
    a = Matriz([[1, 2], [3, 4]])
    b = Matriz([[5, 6], [7, 8]])
    r = a * b
    print(r)