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
    def column(self,columna):
        cols = []
        for i in self.celdas:
            cols.append(i[columna])
        return cols
     
    def __mul__(self, other):
        nueva_matriz=[[0,0],[0,0]]
        for fila in range(len(self.celdas)):
            for columna in range(len(self.celdas)):
                col=other.column(columna)
                m1=self.celdas[fila][0] * col[0] + self.celdas[fila][1]*col[1]
                nueva_matriz[fila][columna]=m1
        print(nueva_matriz)

        return Matriz(nueva_matriz)

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           