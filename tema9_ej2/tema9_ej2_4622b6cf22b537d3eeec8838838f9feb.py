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
        # Verificar si el número de columnas de la primera matriz coincide con el número de filas de la segunda matriz
        if len(self.celdas[0]) != len(other.celdas):
            raise ValueError("No se pueden multiplicar las matrices. El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.")

        # Inicializar una nueva matriz resultante con celdas llenas de ceros
        result = Matriz([[0] * len(other.celdas[0]) for _ in range(len(self.celdas))])

        # Realizar la multiplicación de las matrices
        for i in range(len(self.celdas)):
            for j in range(len(other.celdas[0])):
                for k in range(len(other.celdas)):
                    result.celdas[i][j] += self.celdas[i][k] * other.celdas[k][j]

        return result

if __name__ == "__main__":
    a = Matriz([[1, 2], [3, 4]])
    b = Matriz([[5, 6], [7, 8]])
    r = a * b
    print(r)

           