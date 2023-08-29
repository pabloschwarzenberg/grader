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
        m=""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                m+="{0: >5} ".format((self.celdas[i][j])*(self.celdas[j][i]))
            m+="\n"
        return m

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           