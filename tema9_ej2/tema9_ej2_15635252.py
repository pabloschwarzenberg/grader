class Matriz:
    def __init__(self,celdas):
        self.celdas=celdas
        self.filas=int(len(celdas))
        try: self.columnas=int(len(celdas[0]))
        except IndexError:
            self.columnas= ""

    def __repr__(self):
        s=""
        for i in range(self.filas):
            for j in range(self.columnas):
                s+="{0: >5} ".format(self.celdas[i][j])
            s+="\n"
        return s

    def __mul__(self, other):
        C = []
        for i in range(self.filas): #filas m1
            C.append([0]*((other.columnas)))
        producto=Matriz(C)
        for i in range(self.filas):
            for j in range(other.filas):
                for k in range(other.columnas):
                  producto.celdas[i][j]+=(int(self.celdas[i][k]))*(int(other.celdas[k][j]))
                         
        return producto

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    print(b.columnas)
    r=a*b
    print(r)
