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
        r=[]
        if len(self.celdas[0])==len(other.celdas):
            for i in range(len(self.celdas)):
                fila=[]
                for j in range(len(other.celdas[0])):
                    celda=0
                    for h in range(len(other.celdas)):
                        celda+=self.celdas[i][h]*other.celdas[h][j]
                    fila.append(celda)
                r.append(fila)
            return Matriz(r)

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           