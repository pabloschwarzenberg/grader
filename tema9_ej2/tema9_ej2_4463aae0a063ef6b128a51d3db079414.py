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
        result=Matriz([[0]*len(other.celdas[0])])
        rappend=result.celdas[0].copy()
        for filas in range(len(self.celdas)-1):
            result.celdas.append(rappend)
        for fila in range(len(self.celdas)):
            for columna in range(len(other.celdas[0])):
                suma=0
                for k in range(len(self.celdas[0])):
                    suma+=self.celdas[fila][k]*other.celdas[k][columna]
                result.celdas[fila][columna]=suma
        return result

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           