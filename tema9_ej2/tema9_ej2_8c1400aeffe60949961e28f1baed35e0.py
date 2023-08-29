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
        c=""
        x=[]
        for i in range(len(self.celdas)):
            x.append([0]*len(self.celdas[0]))
            for j in range(len(self.celdas)):
                for k in range(len(self.celdas)):
                    x[i][j]+=self.celdas[i][k]*other.celdas[k][j]
                c+="{0:>5}".format(x[i][j])
            c+="\n"
        return c

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           