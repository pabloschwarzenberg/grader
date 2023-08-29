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
        d=[]
        for l in range(len(self.celdas)):
            m=[]
            for i in range(len(self.celdas)):
                k=0
                for j in range(len(self.celdas)):
                    k+=(other.celdas[j][i]*self.celdas[l][j])
                m.append(k)
            d.append(m)
        m=Matriz(d)
        return m




        return self

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           