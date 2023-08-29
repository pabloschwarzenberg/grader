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
            raise ValueError("Las matrices no se pueden multiplicar")

        result = []
        for i in range(len(self.celdas)):
            row = []
            for j in range(len(other.celdas[0])):
                value = 0
                for k in range(len(other.celdas)):
                    value += self.celdas[i][k] * other.celdas[k][j]
                row.append(value)
            result.append(row)

        return Matriz(result)

if __name__ == "__main__":
    matriz1 = Matriz([[1, 2], [3, 4]])
    matriz2 = Matriz([[5, 6], [7, 8]])

    resultado = matriz1 * matriz2
    print(resultado)