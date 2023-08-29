class Matriz:
    def __init__(self,celdas=[]):
        self.celdas=celdas
        self.dim = (len(self.celdas[0]), len(self.celdas[1]))

    def __repr__(self):
        s=""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s+="{0: >5} ".format(self.celdas[i][j])
            s+="\n"
        return s

    def get(self,i,j):
        if (i) <= self.dim[0] and (j) <= self.dim[1]:
            return self.celdas[i-1][j-1]
        else:
            return None

    def __mul__(self, other):
        new_mat = []

        for r in range(1,self.dim[0]+1):
            new_row = []
            res = 0
            for c in range(1,other.dim[0]+1):
                res += (self.get(r,c) * other.get(c,r))
                new_row.append(res)
            new_mat.append(new_row)
            new_row = []
        return Matriz(new_mat)

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           