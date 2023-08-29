class Matriz:
    def __init__(self, celdas=[]):
        self.celdas = celdas

    def _repr_(self):
        s = ""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s += "{0: >5} ".format(self.celdas[i][j])
            s += "\n"
        return s

    def _mul_(self, other):
        if len(self.celdas[0]) != len(other.celdas):
            raise ValueError("Las dimensiones de las matrices no son compatibles para la multiplicaciÃƒÂ³n.")

        result = Matriz([[0] * len(other.celdas[0]) for _ in range(len(self.celdas))])

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