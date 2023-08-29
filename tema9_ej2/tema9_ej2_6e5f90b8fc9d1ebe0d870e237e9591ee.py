class Matriz:
    def __init__(self, celdas=[]):
        self.celdas = celdas


    def largo(self):
        k=len(self.celdas)
        return k
    def __repr__(self):


        s = ""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s += "{0: >5} ".format(self.celdas[i][j])
            s += "\n"
        return s

    def __mul__(self, other):
        k= len(self.celdas)
        for i in range(0,k):
            for j in range(0,k):
                mr = int(self.celdas[i][j])  *  int(other[j][i])
                self.celdas[i][j] = mr
        r=self.celdas

        return r

if __name__ == "__main__":
    a=Matriz([[1,2],[3,4]])
    b=Matriz([[5,6],[7,8]])
    r=a*b
    print(r)
           