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

    def __mul__(self, otro):
        if len(self.celdas) == 0 or len(otro.celdas) == 0:
            return Matriz()
        
        fila_self = len(self.celdas)
        col_self = len(self.celdas[0])
        fila_other = len(otro.celdas)
        col_other = len(otro.celdas[0])

        if col_self != fila_other:
            raise ValueError("Las matrices no se pueden multiplicar.")

        res = []
        for i in range(fila_self):
            fila = []
            for j in range(col_other):
                val = 0
                for k in range(col_self):
                    val += self.celdas[i][k] * otro.celdas[k][j]
                fila.append(val)
            res.append(fila)

        return Matriz(res)


if __name__ == "__main__":
    a = Matriz([[1, 2], [3, 4]])
    b = Matriz([[5, 6], [7, 8]])
    r = a * b
    print(r)
