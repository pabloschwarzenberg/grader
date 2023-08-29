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

    def __mul__(a,b):
        a1=a.celdas[0][0]
        a2=a.celdas[0][1]
        a3=a.celdas[1][0]
        a4=a.celdas[1][1]
        b1=b.celdas[0][0]
        b2=b.celdas[0][1]
        b3=b.celdas[1][0]
        b4=b.celdas[1][1]
        c1=a1*b1+a2*b3
        c2=a1*b2+a2*b4
        c3=a3*b1+a4*b3
        c4=a3*b2+a4*b4
        self=Matriz([[c1,c2],[c3,c4]])
        return self

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           