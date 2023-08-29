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
        a11=int(self.celdas[0][0])
        a12=int(self.celdas[0][1])
        a21=int(self.celdas[1][0])
        a22=int(self.celdas[1][1])
        b11=int(other.celdas[0][0])
        b12=int(other.celdas[0][1])
        b21=int(other.celdas[1][0])
        b22=int(other.celdas[1][1])
        c11=a11*b11+a12*b21
        c12=a11*b12+a12*b22
        c21=a21*b11+a22*b21
        c22=a21*b12+a22*b22
        c=Matriz([[c11,c12],[c21,c22]])
        return c

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           