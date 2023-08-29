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
        L = self.celdas
        P = other.celdas
        a1=L[0][0]*P[0][0]+L[0][1]*P[1][0]
        b1=L[0][0]*P[0][1]+L[0][1]*P[1][1]
        c1=L[1][0]*P[0][0]+L[1][1]*P[1][0]
        d1=L[1][0]*P[0][1]+L[1][1]*P[1][1]
        M=[[a1,b1],[c1,d1]]
        return Matriz(M)

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           