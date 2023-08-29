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
        l = []
        i = self.celdas
        o = other.celdas
        for x in i:
            for a in x:
                for k in o:
                    for b in k:
                        z = a * b
            l.append(z)