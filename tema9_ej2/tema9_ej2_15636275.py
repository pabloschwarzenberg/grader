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
        celdas1 = self.celdas
        celdas2 = other.celdas
        celdas3 = []
        for i in range(len(celdas1)):
            celdas3.append([0]*(len(celdas2[0])))
        for i in range(len(celdas1)):
            for j in range(len(celdas2)):
                for k in range(len(celdas2[0])):
                    celdas3[i][j] += celdas1[i][k]*celdas2[k][j]
        self.celdas = celdas3
        return self


if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
