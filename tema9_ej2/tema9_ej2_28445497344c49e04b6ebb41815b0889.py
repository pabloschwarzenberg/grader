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
        d = len(self.celdas)
        mr = []
        i = 0
        while i < d:
            j=0
            filai = []
            while j < d:
                mij = 0
                for a in range(d):
                    mij += self.celdas[i][a] * other.celdas[a][j]
                filai.append(mij)
                j += 1
            mr.append(filai)
            i += 1
        r=Matriz(mr)
        return r

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           