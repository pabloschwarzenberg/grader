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
         fila_a=len(self.celdas)
         columna_a=len(self.celdas[0])
         fila_b=len(other.celdas)
         columna_b=len(other.celdas[0])
         c=[0,0]
         #for i in range(fila_a):
           #  c.append(([0]*columna_b))
         for i in range(fila_a):
             for j in range(fila_b):
                 for k in range(columna_b):
                     c[i-1][j-1]+=self.celdas[i-1][k-1]*other.celdas[k-1][j-1]

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    print(a*b)
           