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
        n = len(self.celdas)
        m =len(self.celdas[0])
        m1 = len(other.celdas)
        p = len(other.celdas[0])
        C = []
        #Crea una matriz C vacia de nxp dimensiones
        for l in range(n):
            d=[]
            for t in range(p):
                d.append(0)
            C.append(d)
        #----------------------------------------
        #Actualiza los valores de C 
        for i in range(n):
            for j in range(p):
                suma = 0
                for k in range(m):
                    suma += self.celdas[i][k] * other.celdas[k][j]
                C[i][j] = suma
        return Matriz(C)

if __name__ == "__main__":
    a=Matriz([[1,5],[3,4]])
    b=Matriz([[5,6],[7,-8]])
    r=a*b
    print(r)