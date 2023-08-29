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
        # Verificar que el número de columnas de la primera matriz es igual al número de filas de la segunda matriz
        if len(self.celdas[0]) != len(other.celdas):
            raise ValueError("No se pueden multiplicar las matrices")

        # Inicializar la matriz resultante con ceros
        result = [[0 for j in range(len(other.celdas[0]))] for i in range(len(self.celdas))]

        # Realizar la multiplicación
        for i in range(len(self.celdas)):
            for j in range(len(other.celdas[0])):
                for k in range(len(self.celdas[0])):
                    result[i][j] += self.celdas[i][k] * other.celdas[k][j]

        return Matriz(result)


if __name__ == "__main__":
    a = Matriz([[1, 2], [3, 4]])
    b = Matriz([[5, 6], [7, 8]])
    r = a * b
    print(r)
