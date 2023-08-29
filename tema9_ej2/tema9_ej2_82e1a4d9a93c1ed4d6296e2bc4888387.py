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

    '''def __mCero__(self):
        cero = []
        for i in range(len(self.celdas)):
            fila = []
            for j in range(len(self.celdas)):
                fila.append(0)
            cero.append(fila)
        return Matriz(cero)
    '''

    def __mul__(self, other):
        cero = []
        for i in range(len(self.celdas)):
            fila = []
            for j in range(len(self.celdas)):
                fila.append(0)
            cero.append(fila)


        r = Matriz(cero)
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                x = 0
                y = 0
                producto = 0
                for factor in range(len(self.celdas)):
                    print('r=', r.celdas[i][j])
                    print(self.celdas[i][x], other.celdas[y][j])
                    r.celdas[i][j] += self.celdas[i][x] * other.celdas[y][j]
                    x += 1
                    y += 1
                    print('posicion',i,j,'parcial', r.celdas[i][j])
        return r

