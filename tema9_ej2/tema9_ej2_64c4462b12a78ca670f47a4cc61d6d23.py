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
        s = []
        for i in range(len(self.celdas)): #filas en self
            n = []
            for j in range(len(other.celdas[0])): #columnas en other
                a = 0
                for k in range(len(self.celdas[0])): #columnas  en self y filas en other
                    a += other.celdas[k][j] * self.celdas[i][k]
                n.append(a)
            s.append(n)
        return Matriz(s)

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           