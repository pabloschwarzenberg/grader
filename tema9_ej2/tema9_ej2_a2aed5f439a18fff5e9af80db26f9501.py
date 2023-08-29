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
        m1 = self.celdas
        m2 = other.celdas
        mf = []
        m3 = []
        for i in range(len(m1)):
            for j in range(len(m2)):
                pos=0
                for h in range(len(m1)):
                    pos += (m1[i][h] * m2[h][j])
                m3.append(pos)
            mf.append(m3)
            m3 = []
        M = Matriz(mf)
        return M



if __name__ == "__main__":
    a = Matriz([[1, 2], [3, 4]])
    b = Matriz([[5, 6], [7, 8]])
    r=a*b
    print(r)