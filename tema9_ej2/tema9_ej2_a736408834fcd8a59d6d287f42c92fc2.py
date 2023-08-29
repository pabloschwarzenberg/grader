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
        if len(self.celdas) != len(other.celdas):
            raise ValueError("Las matrices deben tener las mismas dimensiones para multiplicarse.")
        
        n = len(self.celdas)
        m = len(self.celdas[0])
        p = len(other.celdas[0])

        result = [[0 for _ in range(p)] for _ in range(n)]

        for i in range(n):
            for j in range(p):
                for k in range(m):
                    result[i][j] += self.celdas[i][k] * other.celdas[k][j]

        return Matriz(result)


if __name__ == "__main__":
    a = Matriz([[1, 2], [3, 4]])
    b = Matriz([[5, 6], [7, 8]])
    r = a * b
    print(r)
