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
        # Verificar si las matrices son compatibles para multiplicación
        if len(self.celdas) != len(other.celdas[0]):
            raise ValueError("Las matrices no son compatibles para la multiplicación")

        # Crear una nueva matriz para almacenar el resultado de la multiplicación
        resultado = [[0] * len(other.celdas[0]) for _ in range(len(self.celdas))]

        # Realizar la multiplicación de las matrices
        for i in range(len(self.celdas)):
            for j in range(len(other.celdas[0])):
                for k in range(len(other.celdas)):
                    resultado[i][j] += self.celdas[i][k] * other.celdas[k][j]

        return Matriz(resultado)


if __name__ == "__main__":
    a = Matriz([[1, 2], [3, 4]])
    b = Matriz([[5, 6], [7, 8]])
    r = a * b
    print(r)
