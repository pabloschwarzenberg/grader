class Matriz:
    def __init__(self, celdas):
        self.celdas=celdas

    def __repr__(self):
        s=""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s+="{0: >5} ".format(self.celdas[i][j])
            s+="\n"
        return s

    def __mul__(self, other):
        fin=([0,0],[0,0])
        fin[0][0]+=a[0][0]*b[0][0] + a[0][(1)]*b[(1)][0]
        fin[0][1]+=a[0][0]*b[0][1] + a[0][(1)]*b[(1)][1]
        fin[1][0]+=a[1][0]*b[0][0] + a[1][(1)]*b[(1)][0]
        fin[1][1]+=a[1][0]*b[0][1] + a[1][(1)]*b[(1)][1]
        return (fin)


if __name__ == "__main__":
    a=[1,2],[3,4]
    b=[5,6],[7,8]
    r=Matriz.__mul__(a, b)
    print(r)
           