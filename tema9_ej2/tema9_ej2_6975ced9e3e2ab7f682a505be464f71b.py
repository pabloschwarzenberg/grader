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
        r = []
        for i in range (len(self.celdas)):
            f = []
            for j in range(len(self.celdas)):
                s = 0
                for k in range(len(self.celdas)):
                    s += self.celdas[i][k] * other.celdas[k][j]
                f.append(s)
            r.append(f)

        return Matriz(r)




if __name__ == "__main__":
    a = Matriz([[1, 2], [3, 4]])
    b = Matriz([[5, 6], [7, 8]])
    r = a * b
    print(r)
