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
            raise ValueError("Las matrices no se pueden multiplicar")

        # Crear una matriz vacía para almacenar el resultado
        result = [[0] * len(other.celdas[0]) for _ in range(len(self.celdas))]

        # Realizar la multiplicación de matrices
        for i in range(len(self.celdas)):
            for j in range(len(other.celdas[0])):
                for k in range(len(other.celdas)):
                    result[i][j] += self.celdas[i][k] * other.celdas[k][j]

        return Matriz(result)
           