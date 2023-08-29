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
        # Verificar si el número de columnas de la primera matriz es igual al número de filas de la segunda matriz
        if len(self.celdas[0]) != len(other.celdas):
            raise ValueError("No se pueden multiplicar las matrices")

        # Crear una matriz resultante de dimensiones adecuadas
        filas = len(self.celdas)
        columnas = len(other.celdas[0])
        result = [[0] * columnas for _ in range(filas)]

        # Realizar la multiplicación de matrices
        for i in range(filas):
            for j in range(columnas):
                for k in range(len(other.celdas)):
                    result[i][j] += self.celdas[i][k] * other.celdas[k][j]

        return Matriz(result)


if __name__ == "__main__":
    a = Matriz([[1, 2], [3, 4]])
    b = Matriz([[5, 6], [7, 8]])
    r = a * b
    print(r)
           