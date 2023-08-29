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
        z = []
        for j in range(0, int(len(other.celdas))):
            p = []
            for i in range(0, int(len(other.celdas))):
                p.append(other.celdas[i][j])
            z.append(p)

        matriz_producto = []
        for i in range(0, int(len(self.celdas))):
            a = self.celdas[i]
            mr = []
            for j in range(0, int(len(a))):
                b = z[j]
                p = 0
                for k in range(0, int(len(a))):
                    a[k]
                    b[k]
                    p = p + a[k] * b[k]
                mr.append(p)
            matriz_producto.append(mr)
        self.celdas=matriz_producto
        return self


if __name__ == "__main__":
    a = Matriz([[1, 2], [3, 4]])
    b = Matriz([[5, 6], [7, 8]])
    r = a * b
    print(r)
