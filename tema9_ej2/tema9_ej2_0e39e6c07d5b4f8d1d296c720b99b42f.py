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
        A= self.celdas
        B= other.celdas
        AB = [[0 for k in range(len(B[0]))] for j in range(len(A))]
        for i,row in enumerate(A):
            for j,col in enumerate([list(c) for c in zip(*B)]):
                AB[i][j] = sum([a*b for a,b in zip(row,col)])

        

        self.celdas= AB
        return self

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           