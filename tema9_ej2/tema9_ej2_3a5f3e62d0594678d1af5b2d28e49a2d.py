class Matriz:
    def __init__(self,celdas=[]):
        self.fila11=celdas[0][0]
        self.fila12=celdas[0][1]
        self.fila21=celdas[1][0]
        self.fila22=celdas[1][1]

    def __repr__(self):
        s=""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s+="{0: >5} ".format(self.celdas[i][j])
            s+="\n"
        return s

    def __mul__(self, other):
        r1=self.fila11*other.fila11+self.fila12*other.fila21
        r2=self.fila11*other.fila12+self.fila12*other.fila22
        r3=self.fila21*other.fila11+self.fila22*other.fila21
        r4=self.fila21*other.fila12+self.fila22*other.fila22
        return [[r1,r2],[r3,r4]]

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b           