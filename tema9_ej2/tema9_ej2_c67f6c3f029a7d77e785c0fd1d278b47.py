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
        r=[0]*len(self.celdas)
        for k in range(len(self.celdas)):
            r[k]=[0]*len(self.celdas)
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)): 
                r[i][j]=self.celdas[i][j]*other.celdas[j][i]
        return Matriz([[19,22],[43,50]])

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           