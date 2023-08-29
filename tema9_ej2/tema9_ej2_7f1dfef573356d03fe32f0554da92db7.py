class Matriz:
    def __init__(self,celdas=[]):
        self.celdas=celdas

    def __repr__(self):
        s=""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s+="{0: >5} ".format(self.celdas[i][j])
            s+="\n"
        return s

    def __mul__(self, other):
        g = []
        d = []
        h = 0
        for i in range(len(self.celdas)):
            for k in range(len(other.celdas[0])):
                for j in range(len(other.celdas[0])):
                    h += self.celdas[i][j] * other.celdas[j][k]
                d.append(h)
                h = 0
            g.append(d)
            d = []
        return Matriz(g)
           