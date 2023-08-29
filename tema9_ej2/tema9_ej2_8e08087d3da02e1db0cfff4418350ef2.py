class Matriz:
    def init(self, celdas=[]):
        self.celdas = celdas

    def repr(self):
        s = ""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s += "{0: >5} ".format(self.celdas[i][j])
            s += "\n"
        return s

    def mul(self, other):
        if len(self.celdas) != len(other.celdas[0]):
            raise ValueError("Las matrices no son multiplicables")

        result = Matriz([[0 for  in range(len(other.celdas[0]))] for  in range(len(self.celdas))])

        for i in range(len(self.celdas)):
            for j in range(len(other.celdas[0])):
                for k in range(len(other.celdas)):
                    result.celdas[i][j] += self.celdas[i][k] * other.celdas[k][j]

        return result


if name == "main":
    a = Matriz([[1, 2], [3, 4]])
    b = Matriz([[5, 6], [7, 8]])
    r = a * b
    print(r)