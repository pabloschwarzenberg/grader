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

        filas_a = len(self.celdas)
        columnas_a = len(self.celdas[0])
        filas_b = len(other.celdas)
        columnas_b = len(other.celdas[0])

        # Crear matriz resultante llena de ceros
        resultado = Matriz([[0] * columnas_b for _ in range(filas_a)])

        # Realizar multiplicación de matrices
        for i in range(filas_a):
            for j in range(columnas_b):
                for k in range(columnas_a):
                    resultado.celdas[i][j] += self.celdas[i][k] * other.celdas[k][j]

        return resultado


if __name__ == "__main__":
    matriz1 = Matriz([[1, 2], [3, 4]])
    matriz2 = Matriz([[5, 6], [7, 8]])

    resultado = matriz1 * matriz2
    print(resultado)


if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           