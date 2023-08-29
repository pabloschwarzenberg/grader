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

    def __mul__(self,other):
        mult=[]
        for i in range(len(self.celdas)):
            fila=[]
            for j in range(len(self.celdas)):
                a=0
                for k in range(len(self.celdas)):
                    a+=self.celdas[i][k]*other.celdas[k][j]
                fila.append(a)
            mult.append(fila)
        return Matriz(mult)