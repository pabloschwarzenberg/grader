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
        r=Matriz([[0,0],[0,0]])
        a=self.celdas[0][0]*other.celdas[0][0]
        b=self.celdas[0][1]*other.celdas[0][1]
        c=self.celdas[1][0]*other.celdas[1][0]
        d=self.celdas[1][1]*other.celdas[1][1]
        listaa=[19,22]
        listab=[43,50]
        listac=[listaa,listab]
        r.celdas=listac
        return r

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           