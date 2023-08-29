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
            raise ValueError("No se pueden multiplicar las matrices. El número de columnas de la primera matriz debe coincidir con el número de filas de la segunda matriz.")

        resultado = [[0 for _ in range(len(other.celdas[0]))] for _ in range(len(self.celdas))]
        for i in range(len(self.celdas)):
            for j in range(len(other.celdas[0])):
                for k in range(len(other.celdas)):
                    resultado[i][j] += self.celdas[i][k] * other.celdas[k][j]
        return Matriz(resultado)
