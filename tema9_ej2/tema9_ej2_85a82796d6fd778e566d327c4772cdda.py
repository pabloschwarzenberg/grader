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
        if len(self.celdas) != len(other.celdas[0]):
            raise ValueError("No se pueden multiplicar las matrices. El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.")

        filas_resultado = len(self.celdas)
        columnas_resultado = len(other.celdas[0])
        resultado = [[0] * columnas_resultado for _ in range(filas_resultado)]

        for i in range(filas_resultado):
            for j in range(columnas_resultado):
                suma = 0
                for k in range(len(self.celdas[0])):
                    suma += self.celdas[i][k] * other.celdas[k][j]
                resultado[i][j] = suma

        return Matriz(resultado)


if __name__ == "__main__":
    a = Matriz([[1, 2], [3, 4]])
    b = Matriz([[5, 6], [7, 8]])
    r = a * b
    print(r)
