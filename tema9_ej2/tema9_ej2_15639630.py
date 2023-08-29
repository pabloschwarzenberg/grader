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
        m1 = self.celdas
        m2 = other.celdas
        mr = []
        m2_trans = []
        for i in range(len(m2)):
            m2_trans.append([])
        for fila in m2:
            for j in range(len(fila)):
                m2_trans[j].append(fila[j])
        for fila in m1:
            fila_nueva = []
            for col in m2_trans:
                fila_nueva.append(sum(fila[i]*col[i] for i in range(len(fila))))
            mr.append(fila_nueva)
        return Matriz(celdas=mr)

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           